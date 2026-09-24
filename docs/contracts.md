# Shared JSON contracts, version 1.0

These are project recommendations implemented as CPU software validation, not
paper-provided schemas or verified model outputs. The plain dictionaries are
validated by `sdp_xray.common.contracts`; no model framework is imported. All
listed fields are required; unknown fields and unsupported versions are rejected.
Each object carries `schema_version: "1.0"` at its top level.

## Scan input

`validate_scan_input(value)` accepts `schema_version`, an externally assigned
nonempty `scan_id`, and a nonempty `image_path`. Validation checks the structure;
it does not open the file or claim the input exists. `p1.predict(scan_input)` is
reserved and always raises `NotImplementedError`.

## Scan result

`validate_scan_result(value)` validates the following fields:

| Field | Meaning |
| --- | --- |
| `scan_id` | Externally assigned nonempty scan identifier. |
| `status` | `ok`, `missing_input`, or `error`. |
| `image` | Original `width` and `height`, both positive integer pixels. May be `null` on failures when dimensions are unknown. |
| `model` | Nonempty strings `id`, `task`, and `provenance`. Use an explicit task identity such as the actual task-specific annotation namespace. |
| `run` | Nonempty strings `id` and `provenance`. |
| `threshold` | Finite score in [0, 1], recording this result's operating threshold. |
| `detections` | List of detection objects below. |
| `error` | `null` for `ok`; otherwise an object containing nonempty `code` and `message`. |

Provenance strings reference retained manifests/artifact records. A real model
record must identify upstream revision, checkpoint source/hash, configuration,
and category mapping; a real run manifest must include the reproducibility
information in the execution brief. This small validator checks the references
are present, not that their targets exist or their claims are true. Synthetic
software tests reference their test source and are never experiment records.

Version 1.0 records one model/threshold per result. A future composite P1 run must
retain each stage's model, task, class map and threshold in its referenced manifest;
revise the schema if consumers need those fields directly. The current schema
does not by itself validate a two-stage inference implementation.

Each detection contains:

| Field | Meaning |
| --- | --- |
| `id` | Nonempty identifier unique within this scan. |
| `kind` | `device` or `suspicious_region`; these describe box meaning, not component classes. |
| `box_xyxy` | Four finite numbers `[x_min, y_min, x_max, y_max]` in original-image pixel coordinates, with positive extent and bounds within `[0,width] × [0,height]`. Coordinates describe edges; fractional coordinates are permitted. |
| `category` | Nonempty `namespace` and `label`; use the inspected task-specific map, without inventing category IDs. |
| `confidence` | Finite model score in [0, 1], not a calibrated probability claim. |
| `device_id` | Explicit `null` if association is unknown/unavailable. Otherwise a suspicious region must refer to a `device` detection in the same result. A device itself always uses `null`. |

Associations are supplied by the future pipeline, never inferred by this
validator. It allows unassociated and multiple regions/devices and does not
enforce containment: an association policy still needs an agreed design and
evidence. It also does not apply thresholding or check model scores against the
threshold; the future backend must document which scores it retains.

`ok` with an empty detection list means inference reported no detections.
It does **not** mean benign, safe, or missing input. Failure statuses require an
empty detection list and error details; partial predictions need a future schema
decision. The standalone [generic baseline](first-inference.md) saves real predictions and
overlays using this contract. The P1 benign/modified decision, crop/remapping and evaluation
remain unimplemented.

`dumps_scan_result(value)` validates then serializes JSON;
`loads_scan_result(text)` parses JSON then validates it. Validation raises
`ValueError` and does not modify input dictionaries.

## P2 case input

`validate_case_input(value)` requires `schema_version`, a nonempty externally
supplied `case_id`, nonempty `group_provenance`, a nonempty `scans` list of valid
scan results with distinct scan IDs, and
`component_evidence_status: "not_supplied"`. A case may include failed/missing
scan records so absence of evidence remains visible. The externally supplied
group record should state expected scans and any partial collection; completeness
is not inferred from the list length. Filenames are never used to construct
groupings. Provenance presence does not verify physical association.

Version 1.0 has no component-evidence representation, group outcome, or fusion
algorithm. Complete-threat categories must not be relabeled as components.
Adding component evidence will require an explicit schema revision and verified
label/provenance design. `dumps_case_input` and `loads_case_input` perform the
same validated JSON round-trip as their scan counterparts. `p2.fuse(case_input)`
always raises `NotImplementedError`; its future result schema is undecided.
