"""Training-only membership planning; no image reads, label repairs, or file writes."""

import hashlib
import json
import random
from collections import Counter, defaultdict
from copy import deepcopy

from sdp_xray.model_catalog import get_model
from sdp_xray.training import _digest, _text, category_indices

LABELS = tuple(f"{task}:{name}" for task in ("generic", "specific")
               for name in get_model(f"author-yolov10m-{task}").classes)


def fingerprint(value) -> str:
    """Identity of JSON evidence, not authentication of a reviewer's statement."""
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def reviewed(receipt) -> bool:
    return (isinstance(receipt, dict) and receipt.get("decision") == "approved"
            and _text(receipt.get("owner")) and _text(receipt.get("reference")))


def _inventory(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError("nonempty published-split inventories are required")
    result = {}
    for row in rows:
        if (not isinstance(row, dict) or set(row) != {"id", "sha256", "group", "labels"}
                or type(row["id"]) is not int or row["id"] < 0 or not _digest(row["sha256"])
                or row["id"] in result or not isinstance(row["labels"], list)
                or any(not isinstance(label, str) or label not in LABELS for label in row["labels"])
                or len(set(row["labels"])) != len(row["labels"])):
            raise ValueError("invalid/duplicate inventory identity or reviewed label membership")
        group = row["group"]
        if group is not None and not (_text(group) or (type(group) is int and group >= 0)):
            raise ValueError("physical group must retain its original string/integer type")
        result[row["id"]] = deepcopy(row)
    return result


def partition_findings(train, test) -> dict:
    """IDs are local to each published split; byte/group overlap is recorded explicitly."""
    train, test = _inventory(train), _inventory(test)
    def groups(rows, key):
        found = defaultdict(list)
        for identifier, row in rows.items():
            if row[key] is not None:
                found[json.dumps(row[key])].append(identifier)
        return {key: sorted(value) for key, value in sorted(found.items())}
    train_bytes, test_bytes = groups(train, "sha256"), groups(test, "sha256")
    train_groups, test_groups = groups(train, "group"), groups(test, "group")
    return {
        "within_train": [ids for ids in train_bytes.values() if len(ids) > 1],
        "within_test": [ids for ids in test_bytes.values() if len(ids) > 1],
        "train_test_bytes": [{"sha256": json.loads(key), "train_ids": train_bytes[key],
                              "test_ids": test_bytes[key]}
                             for key in sorted(train_bytes.keys() & test_bytes.keys())],
        "train_test_groups": [{"group": json.loads(key), "train_ids": train_groups[key],
                               "test_ids": test_groups[key]}
                              for key in sorted(train_groups.keys() & test_groups.keys())],
    }


def make_partition(train: list, test: list, policy: dict) -> dict:
    """Seed-17, approximately 80/20 whole-component split of published TRAIN only.

    Each inventory row contains id, verified byte sha256, group (or null), and
    reviewed task-prefixed label memberships. Labels from BOTH tasks allow one
    shared, best-effort stratified assignment. Groups are supplied, never inferred.
    A receipt records a human assertion; it is not cryptographic approval.
    """
    training, testing = _inventory(train), _inventory(test)
    findings = partition_findings(train, test)
    if (not isinstance(policy, dict) or not reviewed(policy.get("review"))
            or policy.get("findings_sha256") != fingerprint(findings)
            or policy.get("duplicate_action") != "preserve_and_group"
            or policy.get("test_overlap_action") != "preserve_and_report"
            or not _text(policy.get("label_review_reference"))):
        raise ValueError("reviewed dispositions bound to the exact findings are required")
    mode = policy.get("grouping")
    if mode == "verified_physical":
        if not _text(policy.get("group_key")) or not reviewed(policy.get("physical_group_evidence")) or any(
            row["group"] is None for row in [*training.values(), *testing.values()]
        ):
            raise ValueError("verified physical grouping requires complete external evidence")
    elif mode == "exploratory_exact_bytes":
        if policy.get("group_key") is not None or any(
            row["group"] is not None for row in [*training.values(), *testing.values()]
        ):
            raise ValueError("do not discard supplied physical groups through a fallback")
    else:
        raise ValueError("explicit physical grouping or exploratory fallback required")

    # Union both relations: A shares bytes with B, B shares a group with C => A/B/C together.
    parent = {identifier: identifier for identifier in training}
    def root(identifier):
        while parent[identifier] != identifier:
            parent[identifier] = parent[parent[identifier]]
            identifier = parent[identifier]
        return identifier
    seen = {}
    for identifier, row in sorted(training.items()):
        keys = [("bytes", row["sha256"])]
        if mode == "verified_physical":
            keys.append(("physical", json.dumps(row["group"])))
        for key in keys:
            if key in seen:
                parent[root(identifier)] = root(seen[key])
            seen[key] = identifier
    components = defaultdict(list)
    for identifier in sorted(training):
        components[root(identifier)].append(identifier)
    groups = sorted(components.values())
    if len(groups) < 2:
        raise ValueError("group constraints leave no nonempty fit/validation partition")
    random.Random(17).shuffle(groups)
    groups.sort(key=len, reverse=True)  # Stable seeded ties, large components first.
    totals = Counter({label: 0 for label in LABELS})
    totals.update(label for row in training.values() for label in row["labels"])
    target = len(training) * 0.2
    def cost(ids):
        counts = Counter(label for i in ids for label in training[i]["labels"])
        return abs(len(ids) - target) / len(training) + 0.05 * sum(
            abs(counts[label] - count * 0.2) / max(1, count) for label, count in totals.items()
        ) / max(1, len(totals))
    validation = []
    for group in groups:
        proposed = validation + group
        if len(proposed) < len(training) and cost(proposed) < cost(validation):
            validation = proposed
    if not validation:
        validation = min(groups, key=cost)
    fit = sorted(training.keys() - set(validation))
    validation = sorted(validation)
    counts = {name: {label: sum(label in training[i]["labels"] for i in ids)
                     for label in sorted(totals)}
              for name, ids in (("fit", fit), ("validation", validation))}
    limitations = ["Grouping and stratification are limited to the supplied reviewed evidence.",
                   "A training subset is not proven unseen to supplied task checkpoints."]
    if mode == "exploratory_exact_bytes":
        limitations.append("Exploratory exact-byte groups do not establish physical independence.")
    if findings["train_test_bytes"] or findings["train_test_groups"]:
        limitations.append("Published test overlap is retained and must be reported.")
    result = {
        "schema_version": "t41-partition-1", "origin": "published_train",
        "seed": 17, "validation_fraction_target": 0.2,
        "validation_fraction_actual": len(validation) / len(training),
        "train_inventory": sorted(training.values(), key=lambda row: row["id"]),
        "test_inventory": sorted(testing.values(), key=lambda row: row["id"]),
        "fit_ids": fit, "validation_ids": validation, "policy": deepcopy(policy),
        "findings": findings, "label_image_counts": counts,
        "absent_labels": {split: [label for label, n in values.items() if not n]
                          for split, values in counts.items()},
        "rare_labels_under_five_images": sorted(label for label, n in totals.items() if n < 5),
        "limitations": limitations,
    }
    result["membership_sha256"] = fingerprint(result)
    return result


def validate_partition(partition: dict) -> None:
    expected = make_partition(partition["train_inventory"], partition["test_inventory"],
                              partition["policy"])
    if partition != expected:
        raise ValueError("partition membership/evidence changed; regenerate and review")


def subset_coco(document: dict, partition: dict, split: str, model_id: str) -> dict:
    """Return a derived in-memory view; preserve original IDs/labels and empty images.

    This does not clear geometry or source identity. Use convert_coco and complete
    image audits before any future training. No 'test' subset or trainer fallback.
    """
    validate_partition(partition)
    category_indices(model_id, document["categories"])
    if split not in ("fit", "validation"):
        raise ValueError("only fit/validation views of published training are permitted")
    images = document["images"]
    if (len(images) != len(partition["train_inventory"])
            or {row["id"] for row in images} != {row["id"] for row in partition["train_inventory"]}
            or any(type(row["id"]) is not int for row in images)):
        raise ValueError("task image membership does not match the shared training inventory")
    ids = set(partition[split + "_ids"])
    all_ids = {row["id"] for row in images}
    if any(row.get("image_id") not in all_ids for row in document["annotations"]):
        raise ValueError("unknown image reference; no annotation may be silently discarded")
    result = deepcopy(document)
    result["images"] = [row for row in result["images"] if row["id"] in ids]
    result["annotations"] = [row for row in result["annotations"] if row["image_id"] in ids]
    return result
