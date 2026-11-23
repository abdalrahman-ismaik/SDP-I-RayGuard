# Single-scan data policy: duplicates, invalid boxes and grouping (proposal)

**Status: execution authorized by the user on 22 Nov 2026; Abd's separate review
is not claimed.** Drafted for T41/T42 review by Ahmed, with Abd coordinating.

The later user instruction to proceed without further human approval supersedes
the earlier review wait. Both training-only derived repairs and the shared seed-17
partition have now executed: 9,779 fit and 2,445 validation images. The final
preparation check confirmed all original annotation hashes unchanged. Exact-byte
grouping and the exploratory qualification remain. The example receipt below
intentionally remains pending; the real private receipt records user authorization.

**22 November implementation follow-up:** the local changes below address the
three review requests: an explicitly pending example receipt, recorded bbox-area
treatment, and verified published-split identity. They extend Ali's PR22 source
at `ea9a21b`; they are not an approval, commit or update to the remote PR.

Ahmed's agreement covers: the unchanged test set, the shared 80/20 seed-17 split, keeping
identical training images on the same side, and an exploratory label until physical groups
are verified. His condition for the box clamp: verify the five actual boxes and confirm each
overshoot is below 0.001 px, keep the original annotations unchanged, record every change,
and review the implementation before training. The later execution instruction
superseded that review wait after the three supplied review points were addressed.
Findings and the partition are now recorded from real data; no source file was
changed. It applies to the public IEDXray **generic** and **specific**
explosive tasks only.

Sources: the [IEDXray audit](iedxray-audit.md) (executed 22 Sep 2026), the
[evaluation protocol](single-scan-evaluation-protocol.md), and T41 `training_partition.py`
at commit `32091bc` (inspected, not executed here).

## Rules that are not up for change

1. **The published test split stays unchanged.** No test image is moved, deleted, relabelled
   or clipped. Test images are used only for the final, frozen comparison.
2. **Validation comes from the published training images only**, as one fixed partition of
   about 80/20 with seed 17. The generic and specific studies share the same image-ID assignment.
3. **No selection on test data.** Tuning, early stopping, checkpoint choice, threshold and seed
   are all chosen on validation only.
4. **Source annotation files are never edited.** Any approved change is a derived copy that
   records the source file hash, the affected IDs, the original and new values, and the reason.

## Findings and proposed handling

| # | Finding (audit) | Affects | Proposed handling | T41 policy field |
|---|---|---|---|---|
| 1 | 5 exact-duplicate image pairs within train | Partition | Keep both copies and put them on the **same side** (fit or validation). | `duplicate_action: "preserve_and_group"` |
| 2 | 4 exact-duplicate pairs across train/test: Train005219/Test001859, Train007581/Test002780, Train007583/Test002859, Train012221/Test004750 | Training and test | Keep all 8 images where they are. List the 4 test images in every report (already in the protocol's `flagged_images`). Do not report a "cleaned" primary score. | `test_overlap_action: "preserve_and_report"` |
| 3 | 112 exact-duplicate pairs within test | Test | Keep them. Report that per-image test results are not independent. | (report limitation) |
| 4 | 5 train threat boxes extend outside the image | Training labels | See [invalid boxes](#invalid-boxes). Verified training-only derived repairs executed under user authorization. | Strict post-repair geometry checks |
| 5 | No physical-configuration group data was supplied | Partition | Use exact-byte grouping as a minimum guard. Mark the partition **exploratory**. Do not invent groups from filenames. | `grouping: "exploratory_exact_bytes"`, `group_key: null` |
| 6 | Modified hosts with no threat box: train image IDs 1, 2, 4969, 4970, 4971 and test image ID 71 | Training and test labels | Keep unchanged. List these as known label questions. They are not proof of a benign image. | `label_review_reference` → this section |
| 7 | Mobile/Pager disagreement between exports (4,955 boxes) | Device task only | Out of scope here. The device task stays blocked. | — |

Physical independence between fit and validation is **not** established under rule 5. Any
validation score must carry that caveat. If the lab or model owners supply real group data
later, switch to `grouping: "verified_physical"` with that evidence and regenerate the partition.

## Invalid boxes

The audit found 13 distinct boundary violations. Eleven extend less than 0.0003 px outside
the image, which is consistent with numerical rounding although the cause is unproven. Two
are about 4 px and 2 px negative top coordinates, and both are **test device** boxes
(`Test001757`, `Test003595`), outside the generic and specific tasks. The five train threat
boxes are therefore among the sub-0.0003 px cases. The 22 November HPC follow-up
checked both real training exports and confirmed exactly five corresponding
findings, all strictly below 0.001 px. See [the findings and hashes](t41-data-policy.md).

Authorized treatment:

- **Test annotations:** no change. COCOeval accepts these boxes as given. The generic and
  specific test exports have no boundary findings.
- **Training, sub-0.001 px overshoot only:** a derived **training-only** annotation copy clamps
  these boxes to the image edge, recording the details from rule 4. This changes each box by
  less than 0.001 px. It does not touch the source files.
- **Anything larger, or any new finding:** stays blocked. It is never clipped automatically.
- The verified repair has now run on both real training exports; all other geometry
  findings remain blocking. This authorization does not permit broader automatic clipping.

Executed implementation: `sdp_xray.box_repair` and `scripts/repair_train_boxes.py`.

- `check` lists every box outside the image, with its overshoot, and changes nothing. Run it
  first on the real generic and specific training files to verify the five boxes.
  Add `--verify-training-source` to check the verified source identity without repairing.
- `repair --expected 5 --output-dir runs/<name>` writes a derived copy plus
  `repair-record.json`. The record holds the source hash and, for each change, the
  annotation, the original and new box, and the overshoot. It also holds two hashes of the
  derived copy: `derived_file_sha256` is the SHA-256 of the written file and is the one to
  compare with `sha256sum`; `derived_content_sha256` is of its canonical JSON form. It
  refuses all of these:
  - test files, unknown/reformatted exports, and content that differs from either verified
    public training export (even if the JSON and image filenames are renamed)
  - any overshoot of 0.001 px or more
  - a count other than `--expected`
  - an existing output directory

  The source file is never written. The proposed area treatment is specified below.
- Repair tests use synthetic fixtures (`tests/test_box_repair.py`). Separate actual
  source checks, training-only repairs and the shared partition have now run.

### Chosen derived-area treatment

The actual affected annotations are box-only: they have no segmentation and their
source `area` equals source bbox width multiplied by height. Recompute `area` as
**derived width × derived height for the five changed annotations only**. This keeps
the derived box-only export internally consistent. Leave every unaffected annotation,
category, image record, source file and test export unchanged. Refuse affected annotations
with segmentation or missing/non-finite/non-positive area rather than inventing mask area.

Repair record schema 1.1 names this treatment in `area_field`; every change records
`source_area` and `derived_area` alongside both boxes. This explicitly supersedes the
earlier proposal to leave source area in a changed derived annotation. It changes
neither the original annotation nor any test data. This treatment executed under
the user's later authorization. The official [COCO evaluator](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py)
uses ground-truth area for area-range filtering, so the treatment is reported rather
than hidden. No equality of model metrics is inferred from the small change.

### Verified split guard

Repair is limited to the two exact public IEDXray training exports inspected inside
Figshare file 60096533, archive SHA-256
`94b691e6a06830e45b84097fad33f937821712b1492272a1300dbad2a4e705f3`.
`verify_training_source` requires their recorded **file-byte SHA-256** and full
**canonical JSON content SHA-256**, including the entire image table, annotations
and categories. It also checks the verified 12,224-image count. The file hashes are
listed in [the data record](t41-data-policy.md); exact content identities are in the
implementation and private read-only inspection record.

The CLI computes the byte hash from the bytes it parses. The content check also
prevents an API caller pairing a known train hash with a different/mixed document.
Filename checks remain additional rejection checks; filenames and overlapping
train/test image IDs do not establish the split. Unknown versions or reserialized
exports require a new provenance review. There is no filename-based override.
Source verification is technical provenance, **not** a human policy approval.

`derived_content_sha256` identifies canonical JSON of the derived annotations;
it is not the SHA-256 of the serialized annotation file or of `repair-record.json`.
Record those file-byte hashes separately when the approved repair is eventually run.

## Policy record for `make_partition`

T41 requires a reviewed policy bound to the exact findings. The template below is the
proposal. The `review` receipt must be filled in by the human reviewer, not by an agent.
`findings_sha256` is computed from the real inventory by whoever owns the data run.

```json
{
  "review": {"decision": "pending", "owner": null, "reference": null},
  "findings_sha256": "<fingerprint(partition_findings(train, test)) from the real inventory>",
  "duplicate_action": "preserve_and_group",
  "test_overlap_action": "preserve_and_report",
  "grouping": "exploratory_exact_bytes",
  "group_key": null,
  "label_review_reference": "docs/single-scan-data-policy.md#findings-and-proposed-handling"
}
```

Inventory rows (`id`, `sha256`, `group`, `labels`) should set `group: null` for every image
under exploratory grouping. Labels are task-prefixed, for example `generic:Explosive`.

## What a report may say

- Validation and test results come from an **exploratory** partition with exact-byte
  grouping only. Physical independence is unverified.
- 4 test images duplicate training images, and 112 test pairs duplicate each other. All are retained.
- Supplied task checkpoints may have seen the whole published training set, so their scores
  on this validation partition are not unseen-data results.

## Decisions needed

1. **Abd/Ahmed:** accept or amend rules 1–5 and the table above.
2. **Abd/Ahmed:** approve or reject the sub-0.001 px training-only clamp. If approved,
   implementation and tests are a separate, reviewed change.
3. **Lab/model owners:** say whether physical-configuration group data exists.
4. **Reviewer:** fill in the `review` receipt. The data-run owner then generates
   `findings_sha256` and the partition.
