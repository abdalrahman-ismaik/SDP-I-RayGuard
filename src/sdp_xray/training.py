"""T41 planning, strict COCO conversion, and candidate inference records.

Training settings belong in a separate training manifest. Candidate predictions
use the unchanged shared run contract. There is no training dispatch in this draft.
"""

import hashlib
import json
import math
import struct
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

from sdp_xray.baseline import write_record
from sdp_xray.common.run_manifest import validate_prediction_set, validate_run_manifest
from sdp_xray.model_catalog import get_model

UPSTREAM_REVISION = "453c6e38a51e9d1d5a2aa5fb7f1014a711913397"
INTENDED_PARENT_SHA256 = "b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff"
SPLITS = ("train", "validation", "test")
PAIRS = (("train", "validation"), ("train", "test"), ("validation", "test"))
APPROVALS = ("data_policy", "source_identity", "annotation_policy", "duplicate_policy",
             "physical_groups", "validation_design", "environment", "scope")
MISSING_DOCUMENTS = ("docs/single-scan-ml-pipeline-plan-2026-11.md", "docs/tasks.md:T41")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _digest(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def category_indices(model_id: str, categories: list[dict]) -> dict[int, int]:
    """Match source IDs AND names, independent of the order of COCO rows."""
    spec = get_model(model_id)
    if not isinstance(categories, list) or any(
        not isinstance(row, dict) or type(row.get("id")) is not int or row["id"] < 0
        for row in categories
    ):
        raise ValueError("categories require nonnegative integer source IDs")
    mapping = {str(row["id"]): row.get("name") for row in categories}
    if len(mapping) != len(categories) or mapping != spec.source_category_map:
        raise ValueError("source category IDs/names must exactly match the selected catalog task")
    return {source: spec.classes.index(mapping[str(source)]) for source in spec.coco_ids}


def convert_coco(path: Path, model_id: str) -> dict[str, str]:
    """Read COCO pixel xywh; return YOLO normalized center-xywh label text in memory.

    This is a conversion check, NOT training clearance. It writes no files, uses
    every image (including empty labels), and rejects loss instead of repairing it.
    Call only on authorized artifacts; this draft exercises synthetic inputs only.
    """
    from sdp_xray.data.audit import audit_coco

    before = _sha256(Path(path))
    report = audit_coco(Path(path))
    if report["ok"] is not True or report["errors"]:
        raise ValueError("COCO structure/geometry audit failed; no conversion produced")
    document = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    indices = category_indices(model_id, document["categories"])
    if not document["images"]:
        raise ValueError("empty image split")
    images = {row["id"]: row for row in document["images"]}
    labels, by_image, seen_paths = {}, {}, set()
    for identifier, row in images.items():
        name = PurePosixPath(row["file_name"].replace("\\", "/"))
        if name.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            raise ValueError("only JPEG/PNG image references are supported by this draft")
        label = str(name.with_suffix(".txt"))
        if label.casefold() in seen_paths:
            raise ValueError("label output collision; no images may be overwritten")
        seen_paths.add(label.casefold())
        labels[label], by_image[identifier] = [], label
    seen_rows = set()
    supported = {"id", "image_id", "category_id", "bbox", "area", "iscrowd", "segmentation"}
    for annotation in document["annotations"]:
        if (set(annotation) - supported or type(annotation.get("iscrowd")) is not int
                or annotation["iscrowd"] != 0 or annotation.get("segmentation", []) != []):
            raise ValueError("unsupported annotation fields/crowd/segmentation; no rows dropped")
        if "area" in annotation and (
            type(annotation["area"]) not in (int, float)
            or not math.isfinite(annotation["area"]) or annotation["area"] < 0
        ):
            raise ValueError("invalid annotation area")
        row = images[annotation["image_id"]]
        x, y, width, height = annotation["bbox"]
        values = ((x + width / 2) / row["width"], (y + height / 2) / row["height"],
                  width / row["width"], height / row["height"])
        # The upstream loader deduplicates float32 rows; detect that loss here.
        packed = struct.pack("4f", *values)
        rounded = struct.unpack("4f", packed)
        if rounded[2] <= 0 or rounded[3] <= 0:
            raise ValueError("box size is lost at trainer float32 precision")
        index = indices[annotation["category_id"]]  # Includes valid source category 0.
        identity = (annotation["image_id"], index, packed)
        if identity in seen_rows:
            raise ValueError("duplicate label at trainer precision; no deduplication allowed")
        seen_rows.add(identity)
        labels[by_image[annotation["image_id"]]].append(
            " ".join([str(index), *(format(value, ".17g") for value in values)]) + "\n"
        )
    if _sha256(Path(path)) != before:
        raise ValueError("source changed during conversion")
    return {name: "".join(rows) for name, rows in labels.items()}


def inspect_training_sources(
    sources: dict[str, tuple[Path, Path]], model_id: str, group_key: str | None = None,
) -> dict[str, Any]:
    """Read-only audit adapter. No split creation, source edits, or model loading.

    sources maps train/validation/test to (COCO JSON, image root). File identity
    is computed; published origin and physical provenance still need human review.
    This function is deliberately NOT exposed by the planning CLI.
    """
    from sdp_xray.data.audit import _image_path, audit_coco

    if set(sources) != set(SPLITS):
        raise ValueError("explicit train, validation and reserved test sources are required")
    spec = get_model(model_id)
    identities, conversions = {}, {}
    for split, (annotation, root) in sources.items():
        annotation, root = Path(annotation), Path(root)
        annotation_hash = _sha256(annotation)
        labels = convert_coco(annotation, model_id)
        document = json.loads(annotation.read_text(encoding="utf-8-sig"))
        inventory = [(row["id"], row["file_name"], _sha256(_image_path(root, row["file_name"])))
                     for row in document["images"]]
        identities[split] = {
            "annotation_sha256": annotation_hash,
            "image_inventory_sha256": hashlib.sha256(
                json.dumps(sorted(inventory), separators=(",", ":")).encode()
            ).hexdigest(),
        }
        conversions[split] = {"images": len(labels), "annotations": len(document["annotations"]),
                              "class_map_sha256": spec.class_map_sha256}
    audits = {f"{left}_{right}": audit_coco(
        Path(sources[left][0]), Path(sources[left][1]),
        Path(sources[right][0]), Path(sources[right][1]), group_key,
    ) for left, right in PAIRS}
    for split, (annotation, _) in sources.items():
        if _sha256(Path(annotation)) != identities[split]["annotation_sha256"]:
            raise ValueError("source changed during audit")
    return {"sources": identities, "conversions": conversions, "audits": audits}


def _audit_blockers(evidence: dict, spec: Any) -> list[str]:
    """Warnings/incomplete checks do not become clearance through audit['ok']."""
    blocked = []
    summaries = {}
    for left, right in PAIRS:
        name = f"{left}_{right}"
        report = evidence.get("audits", {}).get(name, {})
        summary = report.get("summary", {})
        if report.get("ok") is not True or report.get("errors") != []:
            blocked.append(f"audit:{name}:errors_or_missing")
        if report.get("warnings") != []:
            blocked.append(f"audit:{name}:unresolved_warnings")
        for key, split in (("primary", left), ("other", right)):
            row = summary.get(key, {})
            count = row.get("images")
            if (type(count) is not int or count <= 0
                    or type(row.get("image_files_checked")) is not int
                    or row.get("image_files_checked") != count
                    or row.get("image_file_checks") != "complete"
                    or row.get("exact_file_duplicate_groups") != []):
                blocked.append(f"audit:{name}:{split}:image_evidence")
            if (row.get("physical_group_checks") != "complete"
                    or not _text(row.get("physical_group_key"))
                    or type(row.get("physical_group_count")) is not int
                    or not 0 < row["physical_group_count"] <= (count or 0)):
                blocked.append(f"audit:{name}:{split}:physical_groups")
            if spec is None or row.get("category_map") != spec.source_category_map:
                blocked.append(f"audit:{name}:{split}:class_map")
            if split in summaries and summaries[split] != row:
                blocked.append(f"audit:{name}:{split}:inconsistent_summary")
            summaries[split] = row
        overlap = summary.get("split_overlap")
        if not isinstance(overlap, dict) or any(
            overlap.get(key) != value for key, value in {
                "filenames": [], "physical_group_values": [], "exact_file_duplicates": [],
                "exact_file_checks": "checked_available_files", "category_maps_match": True,
            }.items()
        ):
            blocked.append(f"audit:{name}:overlap_evidence")
    for split in SPLITS:
        conversion = evidence.get("conversions", {}).get(split, {})
        summary = summaries.get(split, {})
        if (not conversion or spec is None
                or conversion.get("class_map_sha256") != spec.class_map_sha256
                or conversion.get("images") != summary.get("images")
                or conversion.get("annotations") != summary.get("annotations")
                or type(conversion.get("annotations")) is not int
                or conversion["annotations"] < 0):
            blocked.append(f"conversion:{split}:missing_or_inconsistent")
    return blocked


def training_plan(config: dict, evidence: dict | None = None,
                  missing_documents: tuple[str, ...] = MISSING_DOCUMENTS) -> dict:
    """Create a separate, always execution-blocked training manifest.

    Evidence is caller-supplied audit/receipt data, not cryptographic proof of
    provenance or approval. No config setting enables execution in this draft.
    """
    if isinstance(config, dict) and config.get("schema_version") == "t41-research-1":
        from sdp_xray.training_research import research_plan

        return research_plan(config, evidence, missing_documents)
    config, evidence = deepcopy(config), deepcopy({} if evidence is None else evidence)
    if not isinstance(config, dict) or not isinstance(evidence, dict):
        raise ValueError("config and evidence must be objects")
    object_fields = ("gui_confirmation", "sources", "validation", "hyperparameters",
                     "approvals", "environment")
    if any(config.get(key) is not None and not isinstance(config[key], dict)
           for key in object_fields):
        raise ValueError("configuration sections must be objects or null")
    for key in ("sources", "approvals"):
        if any(value is not None and not isinstance(value, dict)
               for value in (config.get(key) or {}).values()):
            raise ValueError("source identities and approval receipts must be objects or null")
    blocked = [f"document:{name}" for name in missing_documents]
    allowed = {"schema_version", "dataset", "model_id", "intended_parent_checkpoint_sha256",
               "gui_confirmation", "sources", "validation", "hyperparameters", "approvals",
               "environment", "requested_device", "owner", "output_directory"}
    if set(config) != allowed or config.get("schema_version") != "t41-draft-1":
        blocked.append("config:schema")
    if config.get("dataset") != "public_iedxray":
        blocked.append("dataset:public_iedxray_only")
    try:
        spec = get_model(config.get("model_id"))
    except ValueError:
        spec = None
        blocked.append("model:selection_unconfirmed")
    model = None
    if spec is not None:
        model = {"id": spec.id, "task": spec.task, "kind": spec.kind,
                 "recorded_checkpoint_sha256": spec.sha256,
                 "class_map_sha256": spec.class_map_sha256,
                 "model_names": {str(k): v for k, v in spec.names.items()},
                 "source_category_map": spec.source_category_map}
        confirmation = config.get("gui_confirmation") or {}
        if (confirmation.get("model") != model or not _text(confirmation.get("confirmed_by"))
                or not _text(confirmation.get("source_reference"))):
            blocked.append("model:sanitized_gui_confirmation")
        if config.get("intended_parent_checkpoint_sha256") != spec.sha256:
            blocked.append("model:intended_parent_conflicts_with_selection")
    # A supplied digest is never promoted to a hash computed by this planner.
    blocked.append("checkpoint:fresh_byte_verification_required")
    sources = config.get("sources") or {}
    if set(sources) != set(SPLITS) or sources != evidence.get("sources"):
        blocked.append("sources:identity_evidence")
    for split in SPLITS:
        identity = sources.get(split) or {}
        if (set(identity) != {"annotation_sha256", "image_inventory_sha256"}
                or not all(_digest(value) for value in identity.values())):
            blocked.append(f"sources:{split}:missing_hashes")
    validation = config.get("validation") or {}
    if (validation.get("origin") != "published_train_subset"
            or not _text(validation.get("membership_reference"))
            or validation.get("independent_of_author_checkpoint") is not False
            or validation.get("test_used_for_tuning") is not False):
        blocked.append("validation:design_and_author_exposure_unresolved")
    if (sources.get("validation") and sources["validation"] in
            (sources.get("train"), sources.get("test"))):
        blocked.append("validation:train_or_test_fallback")
    try:
        blocked.extend(_audit_blockers(evidence, spec))
    except (AttributeError, KeyError, TypeError, ValueError):
        blocked.append("audit:malformed_evidence")
    parameters = config.get("hyperparameters") or {}
    if set(parameters) != {"epochs", "imgsz", "batch", "lr0", "seed"} or any(
        type(parameters.get(key)) is not int or parameters[key] < minimum
        for key, minimum in (("epochs", 1), ("imgsz", 1), ("batch", 1), ("seed", 0))
    ) or (type(parameters.get("lr0")) not in (int, float)
          or not math.isfinite(parameters["lr0"]) or parameters["lr0"] <= 0):
        blocked.append("hyperparameters:unapproved_or_invalid")
    approvals = config.get("approvals") or {}
    for name in APPROVALS:
        receipt = approvals.get(name) or {}
        if (receipt.get("decision") != "approved" or not _text(receipt.get("owner"))
                or not _text(receipt.get("reference"))):
            blocked.append(f"approval:{name}")
    environment = config.get("environment") or {}
    if (environment.get("upstream_revision") != UPSTREAM_REVISION
            or not _digest(environment.get("lock_sha256"))
            or environment.get("train_save_reload_qualified") is not True
            or not _text(environment.get("qualification_reference"))):
        blocked.append("environment:training_save_reload_unqualified")
    for field in ("requested_device", "owner", "output_directory"):
        if not _text(config.get(field)):
            blocked.append(f"execution:{field}_required")
    if _text(config.get("output_directory")):
        output = Path(config["output_directory"])
        if output.exists() or output.is_symlink():
            blocked.append("execution:output_collision")
    blocked.append("execution:software_draft_only")
    return {
        "schema_version": "t41-training-draft-1", "status": "blocked",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "configuration": config, "model": model, "evidence": evidence,
        "missing_documents": list(missing_documents), "blockers": sorted(set(blocked)),
        "execution": {"training_started": False, "device": None},
        "checkpoint_verification": {"performed_by_this_planner": False, "sha256": None},
        "outputs": {"checkpoint_sha256": None, "metrics": None},
    }


def write_training_manifest(path: Path, manifest: dict) -> None:
    """Validate consistency and create one new planning file; never overwrite."""
    expected = training_plan(manifest["configuration"], manifest["evidence"],
                             tuple(manifest["missing_documents"]))
    expected["created_at_utc"] = manifest["created_at_utc"]
    if manifest != expected:
        raise ValueError("training manifest contradicts its configuration/evidence or draft status")
    payload = json.dumps(manifest, indent=2, sort_keys=True, allow_nan=False) + "\n"
    with Path(path).open("x", encoding="utf-8") as stream:
        stream.write(payload)


def candidate_manifest(
    baseline: dict[str, Any],
    checkpoint: Path,
    run: dict[str, Any],
    results: list[dict[str, Any]],
    *,
    model_id: str = "author-yolov10m-generic",
) -> dict[str, Any]:
    """Build a candidate manifest from an original baseline and actual run metadata.

    The run argument supplies every shared field except schema_version, role,
    status and model. In particular, requested_device and actual device must be
    supplied separately. Results must already identify this run and the candidate
    hash; their identities, boxes and scores are never rewritten.

    The original handoff defaults explicitly to the supplied generic parent.
    Another confirmed pairing requires an explicit model_id. This argument never
    establishes the effective GUI selection. The parent file is not opened.
    """
    validate_run_manifest(baseline)
    spec = get_model(model_id)
    expected_model = {
        "id": spec.id,
        "task": spec.task,
        "kind": spec.kind,
        "checkpoint_sha256": spec.sha256,
        "parent_checkpoint_sha256": None,
        "class_map_sha256": spec.class_map_sha256,
        "model_names": {str(index): name for index, name in spec.names.items()},
        "source_category_map": spec.source_category_map,
    }
    if baseline["role"] != "baseline" or baseline["model"] != expected_model:
        raise ValueError("baseline must match the explicitly selected catalog pairing")
    if not isinstance(run, dict):
        raise ValueError("run metadata must be an object")
    if {"schema_version", "role", "status", "model"} & run.keys():
        raise ValueError("schema_version, role, status and model are set by candidate_manifest")
    if not isinstance(results, list) or not results:
        raise ValueError("candidate results must be a nonempty list of completed scan results")

    digest = hashlib.sha256()
    with Path(checkpoint).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    model = deepcopy(baseline["model"])
    model["parent_checkpoint_sha256"] = model["checkpoint_sha256"]
    model["checkpoint_sha256"] = digest.hexdigest()
    manifest = deepcopy(run)
    manifest.update(
        schema_version=baseline["schema_version"],
        role="candidate",
        status="ok" if all(isinstance(r, dict) and r.get("status") == "ok" for r in results)
        else "error",
        model=model,
    )
    # This also calls validate_run_manifest, requiring requested_device and the
    # parent hash, and rejects predictions belonging to the old checkpoint.
    validate_prediction_set(manifest, results)
    if manifest["device"] is None and any(result["status"] == "ok" for result in results):
        raise ValueError("successful candidate scans require the actual inference device")
    return manifest


def write_candidate_record(
    output: Path,
    baseline: dict[str, Any],
    checkpoint: Path,
    run: dict[str, Any],
    results: list[dict[str, Any]],
    *,
    model_id: str = "author-yolov10m-generic",
) -> dict[str, Any]:
    """Validate and write an already-executed candidate run to a new directory."""
    manifest = candidate_manifest(baseline, checkpoint, run, results, model_id=model_id)
    write_record(Path(output), manifest, results)
    return manifest
