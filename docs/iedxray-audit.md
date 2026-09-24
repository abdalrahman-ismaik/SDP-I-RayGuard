# Local IEDXray inspection — 22 September 2026

**Real-data CPU audit completed with findings.** The user supplied an extracted IEDXray
directory containing 17,360 JPEGs and eight COCO JSON files. All images decoded and matched
their declared dimensions. Four exact-byte image pairs cross train/test; Mobile/Pager labels
disagree between annotation exports; strict box checks found 13 distinct boundary violations.
Do not treat this as cleared training/evaluation data or as model inference evidence.

## Provenance and reproducibility

Local root: ignored `data/IEDXray/`, with `Train`, `Test` and `annotations` directories.
There are 17,368 files totaling 509,190,764 bytes. No archive, checkpoint, group metadata or
local README/license file was supplied. The original source files were not modified.

The [published Figshare v1 metadata](https://api.figshare.com/v2/articles/30784328) lists
CC BY 4.0 and `IEDXray_Data_Descriptor.zip`, 482,371,434 bytes, MD5
`45962e6c4cf2a7acd0d637943f160f58`. **The original ZIP is absent locally**, so that checksum
cannot establish these extracted files' byte identity with the published release. The author
repository provides no verified per-file checksum comparison for these annotations.
Matching published counts establish structural agreement only.

Local annotation SHA-256 values are recorded in `runs/iedxray-audit-2026-09-22/manifest.json`.
Every JPEG has a relative path, size and SHA-256 in `image-inventory.csv`; that inventory's
SHA-256 is `61f78cec2f04d59c32240d11cb8d45892823801e0788e3c250863ba421c060ec`.
The run directory also records exact commands, timings, source-code hashes and dirty Git state.
No dataset/model archive was downloaded, and nothing was published, trained or inferred by a
model during this inspection. Only primary-source metadata was fetched.

To reproduce the full image and complete-annotation check:

```text
uv run --locked python -m sdp_xray.cli audit-coco data/IEDXray/annotations/complete_train.json --image-root data/IEDXray/Train --other data/IEDXray/annotations/complete_test.json --other-image-root data/IEDXray/Test
```

The other three task pairs were audited without image roots. Their image ID, filename, width
and height records were separately proven identical to the complete pair within each split,
so the full image checks apply to their shared image inventory. Their individual reports
honestly retain image-not-checked warnings. `run_audit.py` in the local run directory records
and repeats all four commands; no source edits or dataset conversion occur.

## Actual task inventory

All four tasks contain **12,224 train / 5,136 test images**. Boxes use original-pixel COCO
`[x, y, width, height]`. Image IDs are identifiers: they differ from filename number suffixes
in 1,147 train and 532 test records. Always resolve `file_name` through the image table.

| Annotation prefix (`_train.json` / `_test.json`) | Categories | Train boxes / empty images | Test boxes / empty images |
|---|---:|---:|---:|
| `complete` | 11 | 17,349 / 600 | 8,929 / 349 |
| `device_detection` | 4 | 6,659 / 5,565 | 3,471 / 1,665 |
| `binary_explosive_det` | 1 | 7,582 / 4,642 | 3,204 / 1,932 |
| `specific_explosive_det` | 5 | 7,582 / 4,642 | 3,204 / 1,932 |

These are **annotation-empty counts**, not inferred benign outcomes.

Actual category namespaces, preserving the supplied spelling and IDs:

- Complete: 1 Explosive; 2 Battery; 3 Modified laptop; 4 Modified parts; 5 Modified Mobile phone;
  6 Modified Pager; 7 Modified Walkie Talkie; 8 Laptop; 9 Pager; 10 Mobile Phone; 11 Walkie-Talkie.
- Device: 1 Laptop; 2 Mobile; 3 Pager; 4 Walkie-Talkie. **The Mobile/Pager mapping is unresolved.**
- Generic: **0 Explosive**. Zero is a valid source category ID; do not silently renumber it.
- Specific: 1 IED Explosive; 2 Laptop Explosive; 3 Mobile Phone Explosive; 4 Pager Explosive;
  5 Walkie-Talkie Explosive.

Generic and specific annotation records are identical, including annotation IDs and geometry,
except their category IDs. Each matches one complete `Explosive` or `Modified parts` box.
Complete annotations additionally contain captions. No explicit host-to-region association,
physical-group, case, or split-provenance fields are present. Matching/co-occurring records
do not create an authoritative association identifier or model class-order mapping.

## Findings requiring resolution

**1. Device category disagreements: 4,047 train + 908 test = 4,955 boxes.** Every device box
matches exactly one complete box by `(image_id, bbox)`, with no unmatched or ambiguous joins.
After grouping complete modified/unmodified device names by device type, Mobile/Pager names
disagree for these records. Laptop and Walkie-Talkie names agree.

For example, `Train000001.jpg` is `Modified Pager` in complete annotations and `Mobile` in
device annotations at the same box. Of 1,146 training `Modified Mobile phone` boxes, device
export calls 1 Mobile and 1,145 Pager. Of 696 `Modified Pager` boxes, it calls 693 Mobile and
3 Pager. Test mappings differ again. **A global ID 2/3 swap is not a valid repair.** Neither
export has been independently established as the authoritative correct labeling. All 4,955
comparisons are saved in `device-category-disagreements.csv`; no labels were rewritten.

**2. Four exact image-byte pairs cross the supplied train/test splits:**

| Train filename | Test filename |
|---|---|
| Train005219.jpg | Test001859.jpg |
| Train007581.jpg | Test002780.jpg |
| Train007583.jpg | Test002859.jpg |
| Train012221.jpg | Test004750.jpg |

Their captions/box coordinates are not identical despite identical image bytes. There are also
5 duplicate pairs within train and 112 within test. No missing or unreferenced JPEGs were found.
The paper describes physical-configuration separation (PDF p. 5); that published statement
does not override observed image overlap in these supplied files. Preserve the source split
and obtain a documented evaluation/duplicate policy rather than silently removing test images.
Physical identity beyond exact bytes and near duplicates remain unverified.

**3. Thirteen distinct box-boundary violations**, repeated across relevant task exports:
five train threat boxes and eight test device boxes. Eleven extend less than 0.0003 pixels
outside the image; these are consistent with numerical rounding, but the cause is not proven.
Two test device boxes have negative top coordinates of about 4 pixels (`Test001757.jpg`) and
2 pixels (`Test003595.jpg`). No zero/negative box widths or heights were found. The full
`boundary-findings.csv` contains 31 export rows because the same geometry appears in multiple
tasks. No clipping, tolerance relaxation or source correction was applied.

**4. Threat-empty does not imply benign.** Complete annotations mark modified hosts in train
image IDs 1, 2, 4969, 4970, 4971 and test image ID 71, but no corresponding specific modified-region
box is supplied. The reason is unresolved. Captions and raw labels are not independently verified
ground truth about threat status; the P1 decision rule still needs agreement.

**5. Some source images are shared with STCray.** A bounded comparison of the six previously
reviewed STCray preview images against this full IEDXray hash inventory found two exact matches:
STCray train `NonThreatItems_B1_L10_C1_1.jpg` equals IEDXray `Train007588.jpg`; STCray test
`NONTHREAT_B4_L1_C1_1.jpg` equals `Test003220.jpg`. This is not an exhaustive cross-dataset
audit or proof of a subset relationship. Do not assume independence when mixing/evaluating them.

## Verification and current readiness

The COCO auditor was strengthened to reopen and fully decode each image after `verify()`;
a regression demonstrates that a truncated JPEG can pass header verification but fail decoding.
Ruff passed; the CPU suite passed **85 tests and 37 subtests** in 2.52 seconds. These tests use
synthetic software fixtures, distinct from the real dataset checks above.

| Actual command scope | Exit | Seconds | Findings |
|---|---:|---:|---|
| Generic train/test annotations | 1 | 10.035 | 5 train boundary violations |
| Device train/test annotations | 1 | 7.317 | 8 test boundary violations |
| Specific train/test annotations | 1 | 6.862 | Same 5 train boundary violations |
| Complete train/test with image roots | 1 | 166.379 | 13 boundary violations and 4 shared image hashes |

All 17,360 images decoded and matched declared dimensions; no broken IDs/references, category-map
differences between same-task splits, or missing/corrupt images were found by these checks.
The generic COCO checker does **not** detect cross-task label semantics by itself: the independent
exact-box comparison exposed the Mobile/Pager disagreements. Software success is not a clean-data verdict.

Six real examples were visually reviewed in original, complete, device and specific-threat panels,
covering a disagreement, a bare IED, modified/ordinary laptop annotations and an annotation-empty
scan. The previews are labeled **source annotations, no model inference**.

Ignored `configs/project.local.json` points to the dataset and generic training annotations.
The subsequent [first inference](first-inference.md) established generic checkpoint/config/class
pairing; physical-group metadata remains unresolved. Doctor checks path presence, not compatibility.

The [paper review](iedxray-paper-review.md) confirms that task definitions and the intended
split are already documented, and Figure 4 supports complete-export category totals. The
remaining contradictions need authoritative clarification. Next is a standalone device forward
pass using the supplied checkpoint, alongside the generic reference. Device-label correction,
duplicate/evaluation policy and physical provenance are separate requirements for dependent
training/evaluation. Generic inference does not complete the advisor's two-stage P1 pipeline.
