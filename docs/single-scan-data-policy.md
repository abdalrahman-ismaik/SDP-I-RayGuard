# Single-scan data policy: duplicates, invalid boxes and grouping (proposal)

**Status: proposed; agreed by Ahmed (T41) on 22 Nov 2026; the reviewer's record is still
pending.** Drafted for T41/T42 review by Ahmed, with Abd coordinating.

Ahmed's agreement covers: the unchanged test set, the shared 80/20 seed-17 split, keeping
identical training images on the same side, and an exploratory label until physical groups
are verified. His condition for the box clamp: verify the five actual boxes and confirm each
overshoot is below 0.001 px, keep the original annotations unchanged, record every change,
and review the implementation before training. Ahmed will generate the findings hash and
partition from the real data once the review is recorded.

On 22 Nov Ahmed verified the HPC inputs and confirmed five matching sub-0.001 px box findings
in each training export (generic and specific). No repair, partition or training run was
performed. Abd's 22 Nov message agreed with the policy direction and set conditions for the
training-only clamp. The implementation review receipt remains pending until the human
reviewer records a decision.

Nothing in this proposal changes a source file, and no partition or training
run has been created. It applies to the public IEDXray **generic** and **specific**
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
| 4 | 5 train threat boxes extend outside the image | Training labels | See [invalid boxes](#invalid-boxes). Blocked until reviewed. | (blocked) |
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
boxes are therefore among the sub-0.0003 px cases. This follows from the audit's counts; the
per-box values in the private `boundary-findings.csv` were not re-inspected for this proposal.

Proposal for review:

- **Test annotations:** no change. COCOeval accepts these boxes as given. The generic and
  specific test exports have no boundary findings.
- **Training, sub-0.001 px overshoot only:** a derived **training-only** annotation copy clamps
  these boxes to the image edge, recording the details from rule 4. This changes each box by
  less than 0.001 px. It does not touch the source files.
- **Anything larger, or any new finding:** stays blocked. It is never clipped automatically.
- **Until the implementation is reviewed and run on the real files**, training on these five
  boxes stays blocked.

Implementation, pending review: `sdp_xray.box_repair` and `scripts/repair_train_boxes.py`.

- `check` lists every box outside the image, with its overshoot, and changes nothing. Run it
  first on the real generic and specific training files to verify the five boxes.
- `repair --test-annotations <test.json> --expected 5 --output-dir runs/<name>` writes a derived copy plus
  `repair-record.json`. The record holds the source hash and, for each change, the
  annotation, the original and new box, and the overshoot. It also holds two hashes of the
  derived copy: `derived_file_sha256` is the SHA-256 of the written file and is the one to
  compare with `sha256sum`; `derived_content_sha256` is of its canonical JSON form. It
  refuses all of these:
  - the published test file of the task, identified by its hash, and any training file that
    shares an image file name with it. This guard rests on the published split itself; the
    filename check (`test` in the name) is an extra, not the only guard. The record stores the
    test file's hash and name and confirms zero shared images.
  - any overshoot of 0.001 px or more
  - a count other than `--expected`
  - an existing output directory

  The source file is never written.
- **COCO `area`: kept unchanged from the source.** The YOLO trainer derives labels from
  `bbox`; `area` is not used for training. The frozen T42 validation objective is overall
  AP@[.50:.95] across all area ranges, so retaining source `area` does not change that
  objective. COCOeval's size-specific validation metrics can be affected when validation is
  derived from repaired training annotations; do not interpret those metrics without a
  caveat or a separately justified area policy. Published test annotations are never repaired.
  Each change records the source `area` and the bbox-implied area change, which is below
  0.001 px times the box side (far below one pixel). The record states this treatment in
  `area_field`.
- Synthetic tests only (`tests/test_box_repair.py`). The tool has **not** been run on the
  real annotations, because the dataset is not on the drafting machine.

## Policy record for `make_partition`

T41 requires a reviewed policy bound to the exact findings. The template below is the
proposal. Its decision is **pending**, which `make_partition` rejects, so it cannot pass as
approved. Only the human reviewer changes it to `approved` and fills in owner and reference,
never an agent.
`findings_sha256` is computed from the real inventory by whoever owns the data run.

```json
{
  "review": {"decision": "pending", "owner": "<reviewer name>", "reference": "<PR or minutes link>"},
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
2. **Abd:** approve or reject the clamp implementation (`sdp_xray.box_repair`), now with the
   published-split guard and the recorded `area` treatment.
3. **Lab/model owners:** say whether physical-configuration group data exists.
4. **Reviewer:** fill in the `review` receipt. The data-run owner then generates
   `findings_sha256` and the partition.
