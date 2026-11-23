"""YOLOv10 dataset preparation and conditionally authorized trainer adapter.

The live factory checks the planner before importing the pinned model package.
Dataset preparation is an explicit API, never invoked by the planning CLI.
"""

import json
import math
import shutil
from copy import deepcopy
from pathlib import Path, PurePosixPath

from sdp_xray.training import _sha256, convert_coco
from sdp_xray.training_partition import fingerprint, validate_partition
from sdp_xray.training_research import (
    TASKS,
    inspect_partition_sources,
    protocol_settings,
    require_live_ready,
    research_plan,
    task_identity,
    validate_initialization,
)
from sdp_xray.tuning import validate_objective_result, validate_parameters


def _write_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def _regular_file(root, relative):
    path = root / relative
    if (path.is_symlink() or not path.is_file()
            or not path.resolve().is_relative_to(root.resolve())):
        raise ValueError("bundle/checkpoint must be a regular file inside its owned directory")
    return path


def _integer_randrange(randrange, *bounds):
    """Preserve the fork's integral multi-scale bounds on Python 3.12+."""
    converted = []
    for value in bounds:
        if isinstance(value, float):
            if not value.is_integer():
                raise ValueError("multi-scale random range requires integral bounds")
            value = int(value)
        converted.append(value)
    return randrange(*converted)


def _retain_checkpoints(directory, identities, keep, epoch):
    """Remove only this attempt's verified unselected snapshots, recording hashes."""
    if directory.is_symlink() or not keep or not set(keep) <= identities.keys():
        raise ValueError("retention must preserve known selected checkpoints")
    removed = []
    for name, digest in identities.items():
        path = _regular_file(directory, name)
        if path.parent.resolve() != directory.resolve() or _sha256(path) != digest:
            raise ValueError("checkpoint identity changed before retention")
        if name not in keep:
            removed.append({"file": name, "sha256": digest, "bytes": path.stat().st_size})
    if not removed:
        return
    record = {"policy": "best_validation_and_latest", "epoch": epoch,
              "kept": {name: identities[name] for name in sorted(keep)}, "removed": removed}
    _write_json(directory / f"retention-{epoch:03d}-planned.json", record)
    for row in removed:
        (directory / row["file"]).unlink()
        del identities[row["file"]]
    _write_json(directory / f"retention-{epoch:03d}-completed.json", record)


def prepare_training_bundle(config, sources, partition, output):
    """Copy reviewed fit/validation inputs to an isolated YOLO dataset; never copy test.

    Reuses the complete auditor/preflight and strict conversion. Source images,
    annotations and the reserved test split are read only. Exercise with synthetic
    sources until real-data processing is separately authorized.
    """
    from sdp_xray.data.audit import _image_path

    output = Path(output)
    if output.exists() or output.is_symlink():
        raise FileExistsError("dataset output already exists")
    for annotation, image_root in sources.values():
        for source in (Path(annotation).resolve(), Path(image_root).resolve()):
            if output.resolve().is_relative_to(source) or source.is_relative_to(output.resolve()):
                raise ValueError("dataset output must be separate from source locations")
    evidence = inspect_partition_sources(sources, config["task"], partition)
    # Preparing reviewed data precedes the pilot that qualifies training. Keep
    # every source/partition/conversion gate, but do not require a completed GPU
    # pilot, starting weights or study compute approval just to copy data.
    data_prefixes = ("config:", "task:", "sources:", "partition:", "data:",
                     "audit:", "conversion:", "validation:")
    data_approvals = {"approval:data_policy", "approval:source_identity",
                      "approval:validation_design"}
    blocked = research_plan(config, evidence)["blockers"]
    if any(item.startswith(data_prefixes) or item in data_approvals for item in blocked):
        raise ValueError("complete reviewed source/partition evidence is required before preparation")
    output.mkdir(exist_ok=False)
    inventory = {row["id"]: row for row in partition["train_inventory"]}
    files, membership = {}, {}
    for split in ("train", "validation"):
        annotation, image_root = sources[split]
        labels = convert_coco(Path(annotation), TASKS[config["task"]])
        document = json.loads(Path(annotation).read_text(encoding="utf-8-sig"))
        (output / "images" / split).mkdir(parents=True)
        (output / "labels" / split).mkdir(parents=True)
        membership[split] = []
        for row in document["images"]:
            name = PurePosixPath(row["file_name"].replace("\\", "/"))
            image = f"images/{split}/{row['id']}{name.suffix.lower()}"
            label = f"labels/{split}/{row['id']}.txt"
            source = _image_path(Path(image_root), row["file_name"])
            with source.open("rb") as incoming, (output / image).open("xb") as outgoing:
                shutil.copyfileobj(incoming, outgoing)
            if _sha256(output / image) != inventory[row["id"]]["sha256"]:
                raise ValueError("image changed after audit; partial bundle is not usable")
            with (output / label).open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(labels[str(name.with_suffix(".txt"))])
            files.update({image: _sha256(output / image), label: _sha256(output / label)})
            membership[split].append({"id": row["id"], "image": image, "label": label})
    # Catch a changed source, including test, before publishing a usable receipt.
    if inspect_partition_sources(sources, config["task"], partition) != evidence:
        raise ValueError("source changed during preparation; partial bundle is not usable")
    names = list(task_identity(config["task"])["model_names"].values())
    data = {"path": str(output.resolve()), "train": "images/train",
            "val": "images/validation", "names": names, "nc": len(names)}
    # JSON is a YAML subset. No YAML dependency or executable download entry is needed.
    _write_json(output / "data.yaml", data)
    files["data.yaml"] = _sha256(output / "data.yaml")
    receipt = {"schema_version": "t41-training-bundle-1", "task": config["task"],
               "partition": partition, "sources": evidence["sources"],
               "membership": membership, "files": files}
    receipt["sha256"] = fingerprint(receipt)
    _write_json(output / "bundle.json", receipt)  # Written last; incomplete outputs are rejected.
    return output


def check_training_bundle(directory, config):
    """Recheck the copied data, maps and source identities; reject validation fallback."""
    root = Path(directory)
    if root.is_symlink():
        raise ValueError("dataset directory must not be a symlink")
    receipt = json.loads(_regular_file(root, "bundle.json").read_text(encoding="utf-8"))
    payload = {key: value for key, value in receipt.items() if key != "sha256"}
    if (receipt["sha256"] != fingerprint(payload)
            or receipt["schema_version"] != "t41-training-bundle-1"
            or receipt["task"] != config["task"] or receipt["sources"] != config["sources"]
            or receipt["partition"]["membership_sha256"] != config["partition_sha256"]):
        raise ValueError("dataset bundle identity differs from the research configuration")
    validate_partition(receipt["partition"])
    expected_files = {"data.yaml"}
    for split, key in (("train", "fit_ids"), ("validation", "validation_ids")):
        rows = receipt["membership"][split]
        if (not rows or sorted(row["id"] for row in rows) != receipt["partition"][key]):
            raise ValueError("fit/validation membership is missing or changed")
        for row in rows:
            suffix = PurePosixPath(row["image"]).suffix
            if (suffix not in (".png", ".jpg", ".jpeg")
                    or row["image"] != f"images/{split}/{row['id']}{suffix}"
                    or row["label"] != f"labels/{split}/{row['id']}.txt"):
                raise ValueError("unexpected training image/label path")
            expected_files.update((row["image"], row["label"]))
    actual_files = {p.relative_to(root).as_posix() for folder in ("images", "labels")
                    for p in (root / folder).rglob("*") if p.is_file()}
    if (set(receipt["files"]) != expected_files or actual_files != expected_files - {"data.yaml"}
            or any(_sha256(_regular_file(root, name)) != digest
                   for name, digest in receipt["files"].items())):
        raise ValueError("copied image/label bytes or coverage changed")
    names = list(task_identity(config["task"])["model_names"].values())
    expected_data = {"path": str(root.resolve()), "train": "images/train",
                     "val": "images/validation", "names": names, "nc": len(names)}
    if json.loads((root / "data.yaml").read_text(encoding="utf-8")) != expected_data:
        raise ValueError("only explicit fit/validation data is allowed; no test or downloads")
    return receipt


def training_arguments(request, weights, bundle):
    """Construct explicit fork arguments, with no imports, model load or dispatch."""
    config = request["configuration"]
    if config["study"] != protocol_settings() or config["experiment"] != "controlled_improvement":
        raise ValueError("trainer requires the frozen controlled-improvement protocol")
    seed, stage = request.get("seed", 17), request.get("stage", "search")
    if (stage not in ("pilot", "search", "confirmation", "repeatability")
            or type(request["epochs"]) is not int
            or (stage == "pilot" and not 1 <= request["epochs"] <= 30)
            or (stage != "pilot" and request["epochs"] != (30 if stage == "search" else 100))
            or (stage != "repeatability" and seed != 17)):
        raise ValueError("run stage, seed or epoch budget differs from the protocol")
    validate_initialization(request["initialization"], config["task"], expected_seed=seed)
    if any(request["initialization"][key] != config["initialization"][key] for key in
           ("checkpoint_sha256", "source_reference", "procedure", "task_head", "task")):
        raise ValueError("run initialization differs from the frozen research configuration")
    if request.get("resume_checkpoint") or request.get("completed_epochs", 0):
        # Upstream check_resume restores old args/save_dir and stripped checkpoints
        # lose optimizer state. Do not claim a safe real continuation yet.
        raise ValueError("YOLO checkpoint resume requires a qualified isolated-output adapter")
    validate_parameters(request["parameters"])
    if (config["precision"] != "float32" or type(config["batch"]) is not int
            or config["batch"] < 1 or config["requested_device"] not in ("cpu", "0")):
        raise ValueError("explicit fixed batch, FP32 and one allocation-relative device required")
    check_training_bundle(bundle, config)
    weights = Path(weights)
    if (not weights.is_absolute() or weights.is_symlink() or not weights.is_file()
            or _sha256(weights) != request["initialization"]["checkpoint_sha256"]):
        raise ValueError("full local weights path and matching byte hash required")
    output = Path(request["output_directory"])
    if not output.is_dir() or output.is_symlink() or any(output.iterdir()):
        raise ValueError("trainer requires a new empty owned attempt directory")
    return {**deepcopy(config["study"]["fixed"]), **deepcopy(request["parameters"]),
            "model": str(weights.resolve()), "data": str((Path(bundle) / "data.yaml").resolve()),
            "task": "detect", "mode": "train", "epochs": request["epochs"], "imgsz": 640,
            "batch": config["batch"], "amp": False, "half": False, "seed": seed,
            "device": config["requested_device"], "workers": 2, "deterministic": True,
            "project": str(output.resolve()), "name": "upstream", "exist_ok": False,
            "resume": False, "time": None, "save": True, "val": True, "val_period": 1,
            "plots": False, "cache": False, "fraction": 1.0, "single_cls": False,
            "patience": 0}  # Disable framework early stop; declared AP controls selection/pruning.


class YoloTrainerAdapter:
    """Pinned trainer API adapter; real classes require the still-blocked live gate."""

    def __init__(self, trainer_class, weights, bundle, *, plan=None, authorization=None,
                 checkpoint_retention="all"):
        if checkpoint_retention not in {"all", "best_validation_and_latest"}:
            raise ValueError("unknown checkpoint retention policy")
        self.checkpoint_retention = checkpoint_retention
        self.synthetic = getattr(trainer_class, "synthetic", False) is True
        self.plan = deepcopy(plan)
        self.authorization = deepcopy(authorization)
        self.training_started = False
        if not self.synthetic:
            if self.plan is None:
                raise ValueError("non-synthetic trainer requires a checked live plan")
            require_live_ready(self.plan, self.authorization)
        self.trainer_class, self.weights, self.bundle = trainer_class, Path(weights), Path(bundle)

    def run_with_callback(self, request, on_epoch):
        self.training_started = False
        if not self.synthetic:
            require_live_ready(self.plan, self.authorization)
            if (request["configuration"] != self.plan["configuration"]
                    or not Path(request["output_directory"]).resolve().is_relative_to(
                        Path(self.plan["configuration"]["output_directory"]).resolve())):
                raise ValueError("trainer request differs from approved configuration/output")
        arguments = training_arguments(request, self.weights, self.bundle)
        output = Path(request["output_directory"])
        snapshots = output / "completed-epochs"
        snapshots.mkdir(exist_ok=False)
        trainer = self.trainer_class(overrides=arguments)
        if any(getattr(trainer.args, key, None) != value for key, value in arguments.items()):
            raise ValueError("upstream changed explicit training controls")
        if Path(trainer.save_dir).resolve() != (output / "upstream").resolve():
            raise ValueError("upstream changed its assigned output directory")
        # Keep all effective defaults in the private training record, outside the
        # strict inference manifest. Fake fixtures never establish runtime defaults.
        _write_json(output / "effective-arguments.json", vars(trainer.args))
        completed, best_value, best_name, identities = 0, None, None, {}

        def saved_epoch(current):
            nonlocal completed, best_value, best_name
            epoch = current.epoch + 1
            if type(current.epoch) is not int or not 1 <= epoch <= request["epochs"]:
                raise ValueError("invalid saved epoch")
            upstream = (output / "upstream").resolve()
            last = _regular_file(upstream, Path(current.last).relative_to(upstream))
            destination = snapshots / f"epoch-{epoch:03d}.pt"
            if epoch <= completed:
                if not destination.is_file() or _sha256(last) != _sha256(destination):
                    raise ValueError("duplicate epoch changed checkpoint bytes")
                return
            if epoch != completed + 1:
                raise ValueError("missing completed epoch")
            with last.open("rb") as incoming, destination.open("xb") as outgoing:
                shutil.copyfileobj(incoming, outgoing)
            if _sha256(destination) != _sha256(last):
                raise ValueError("saved checkpoint changed during copy")
            completed = epoch
            identities[destination.name] = _sha256(destination)
            # Called synchronously: errors/pruning/interrupts stop the trainer now.
            value = on_epoch({"phase": "fit", "completed_epoch": epoch, "checkpoint": destination})
            if self.checkpoint_retention == "best_validation_and_latest":
                if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1:
                    raise ValueError("retention requires the verified validation objective")
                if best_value is None or value > best_value:
                    best_value, best_name = value, destination.name
                _retain_checkpoints(snapshots, identities, {best_name, destination.name}, epoch)

        trainer.add_callback("on_model_save", saved_epoch)
        self.training_started = not self.synthetic
        trainer.train()
        if completed != request["epochs"]:
            raise ValueError("trainer stopped before the declared epoch budget")


class CheckpointValidationAdapter:
    """Private checkpoint-path binding around Ali's portable request/result contract.

    delegate.evaluate_checkpoint(request, checkpoint) must return the existing
    result shape. This adapter supplies no predictions or COCO implementation.
    """

    def __init__(self, delegate):
        self.delegate = delegate
        self.synthetic = getattr(delegate, "synthetic", False) is True

    def evaluate_checkpoint(self, request, checkpoint):
        checkpoint = Path(checkpoint)
        if _sha256(checkpoint) != request["checkpoint_sha256"]:
            raise ValueError("validation checkpoint identity mismatch")
        original = deepcopy(request)
        result = self.delegate.evaluate_checkpoint(deepcopy(request), checkpoint)
        if _sha256(checkpoint) != original["checkpoint_sha256"]:
            raise ValueError("checkpoint changed during validation")
        validate_objective_result(original, result)
        return result


def live_trainer_class(plan, authorization=None):
    """Import only after conditional gates; preserve the scheduler's GPU mask."""
    require_live_ready(plan, authorization)
    import os
    from unittest.mock import patch

    import torch
    import ultralytics.engine.trainer as trainer_module
    from ultralytics.models.yolov10.train import YOLOv10DetectionTrainer

    from sdp_xray.training_checkpoint import checkpoint_loading

    class AllocatedTrainer(YOLOv10DetectionTrainer):
        def __init__(self, overrides):
            mask = os.environ.get("CUDA_VISIBLE_DEVICES")
            if not mask or overrides["device"] != "0" or not torch.cuda.is_available():
                raise ValueError("one allocated CUDA device is required")
            if torch.cuda.device_count() != 1:
                raise ValueError("single visible GPU required; no automatic distributed launch")
            # The pinned select_device normally rewrites CUDA_VISIBLE_DEVICES.
            # Resolve allocation-relative device 0 without changing that mask.
            with patch("ultralytics.engine.trainer.select_device",
                       lambda *args, **kwargs: torch.device("cuda:0")):
                super().__init__(overrides=overrides)
            if os.environ.get("CUDA_VISIBLE_DEVICES") != mask:
                raise ValueError("allocated GPU mask changed")

        def setup_model(self):
            source = Path(self.args.model).resolve()
            with checkpoint_loading({source: plan["configuration"]["initialization"]["checkpoint_sha256"]}):
                return super().setup_model()

        def train(self):
            # The fork writes label caches even with image cache=False. Keep
            # the hash-verified shared bundle immutable between study attempts.
            import ultralytics.data.dataset as dataset_module

            def memory_cache(prefix, path, cache):
                cache["version"] = dataset_module.DATASET_CACHE_VERSION

            with patch.object(dataset_module, "save_dataset_cache_file", memory_cache):
                return super().train()

        def preprocess_batch(self, batch):
            # The pinned fork passes imgsz * 0.5 / 1.5 as integral floats.
            # Python 3.12 removed randrange's implicit conversion. Keep its
            # original range, stride rounding and seeded random generator.
            import random

            original = random.randrange
            with patch.object(random, "randrange", lambda *bounds: _integer_randrange(original, *bounds)):
                return super().preprocess_batch(batch)

        def final_eval(self):
            # Upstream strips and then reloads best.pt. Bind its own last/best
            # outputs, refreshing identity only after that deliberate write.
            identities = {}
            for path in (self.last, self.best):
                if path.exists():
                    checked = _regular_file(Path(self.save_dir), path.relative_to(self.save_dir))
                    identities[checked.resolve()] = _sha256(checked)
            original_strip = trainer_module.strip_optimizer

            def strip(path, *args, **kwargs):
                candidate = Path(path).resolve()
                if candidate not in identities:
                    raise ValueError("finalization checkpoint is outside the owned output")
                result = original_strip(path, *args, **kwargs)
                identities[candidate] = _sha256(candidate)
                return result

            with checkpoint_loading(identities), patch.object(trainer_module, "strip_optimizer", strip), \
                    patch("ultralytics.engine.validator.select_device", lambda *a, **k: torch.device("cuda:0")):
                return super().final_eval()

    return AllocatedTrainer
