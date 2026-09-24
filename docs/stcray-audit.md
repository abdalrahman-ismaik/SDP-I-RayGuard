# Local STCray inspection — 22 September 2026

The available base train/test archives and README are stored under ignored `data/STCray/`.
This is a **real-data CPU audit**, separate from synthetic software tests and model inference.
No checkpoint, model execution, conversion, training or new download is part of this inspection.
STCray remains a secondary dataset: its threat boxes do not establish IEDXray's modified-device
labels or P2 case/group relationships. Neither prototype is complete.

## Source and artifact identity

[Author release](https://huggingface.co/datasets/Naoufel555/STCray-Dataset), revision
`a335afc48b700a1be3516ebb5a0000166d97290b`; card metadata labels Apache-2.0.
The release is gated. This inspection uses locally available artifacts; it does not verify
the authenticated download workflow. Each user must follow the release's access conditions.

| Supplied file | Bytes | Local SHA-256 |
|---|---:|---|
| STCray_TrainSet.rar | 1,094,236,470 | `d003765c0e17775aaebd0c4ce873b7ba493df5a746b59f4b8d34194bf0b5638c` |
| STCray_TestSet.rar | 980,265,948 | `9379a5ad5b292d1024e9155c6666c494b9a3ae80cb0ce91e90215daf46885c65` |
| ReadMe_STCray.docx | 16,106 | `1fd9ceb4f5db05fced33e05c6caa34a032ef3a9bfd8fdcbc3e06152a6d4f2014` |

Public metadata masks the archives' direct LFS SHA-256 fields. Constructing the canonical
[Git LFS pointer](https://github.com/git-lfs/git-lfs/blob/main/docs/spec.md) from each measured
local SHA-256 and size reproduces its published pointer Git blob ID exactly: train
`dd806dbb93154d1670c84a98277b005be27281f5`, test `7d07668f3486f16fe620bcf478cf4d12c248c729`.
This is indirect hash verification through pointer identity, not a directly visible remote hash.
The README's ordinary Git blob ID also matches `1cf109325024df0ebada9cb63950b561758d2a0b`.
[Pinned file metadata](https://huggingface.co/api/datasets/Naoufel555/STCray-Dataset/tree/a335afc48b700a1be3516ebb5a0000166d97290b?recursive=false&expand=false).

## Native layout and scope

Both split directories contain `Images` (JPG), `Json_BB` (rectangle JSON), `Json` (polygon
JSON), `Segmentation` (PNG) and `Captions` (XLSX). The supplied DOCX describes these folders,
but supplies no numeric category map, mask palette semantics or physical-group identifiers.

Actual rectangle records contain `imagePath`, `imageHeight`, `imageWidth` and `shapes`, with
string `label`, `shape_type: rectangle`, and two original-pixel corner points per shape.
This is LabelMe-style per-image data, **not COCO**. Preserve raw label spelling and split identity.
STING-BEE's documented normalized model-output coordinates must not be applied to these raw boxes.

| Archive inventory | Train | Test |
|---|---:|---:|
| JPEG images | 30,044 | 16,598 |
| Rectangle JSON files | 29,444 | 16,249 |
| Polygon JSON files | 29,444 | 16,249 |
| Segmentation PNG files | 29,444 | 16,249 |
| Caption workbooks | 22 | 22 |
| Explicit `Class 22_Non Threat` images | 600 | 349 |
| `Class 21_Multilabel Threat` images | 3,077 | 180 |

All threat image class/stems correspond to all three annotation trees in the archive listings;
only the explicit non-threat folder lacks annotations. The folder numbers are not a verified
detection category map. Multilabel folder membership is not the same as a count of multiple
instances. Four Windows metadata files occur in train (`desktop.ini` / `Thumbs.db`); preserve
them with the source, exclude them from image processing.

UnRAR 6.11 extracted both archives into `data/STCray/extracted/` with exit 0, retaining the originals. Preflight
checked every listed entry for relative paths, the expected split root and File/Directory type.
Combined uncompressed size is 2,455,056,930 bytes across 183,769 files. Disk headroom was checked.

## Reproduce and evidence

```text
uv run --locked python -m sdp_xray.cli audit-stcray data/STCray/extracted
```

The command decodes every JPEG, hashes its exact bytes, checks image-to-rectangle correspondence,
dimensions, label strings and finite nondegenerate rectangle bounds, and compares both splits.
It only reads source files. Findings retain exact occurrence counts and up to five examples per
finding type. Exit 1 means findings needing investigation, not a failed software installation.

Local evidence directory: `runs/stcray-audit-2026-09-22/` (ignored), including `manifest.json`,
`archive-inventory.json`, the audit report, and a ground-truth preview script/selection.
The preview uses supplied annotations, never model predictions. Full-data checks are independent
of the software's synthetic tests.

## Executed results

Full audit: **exit 1**, 470.186 seconds, with actual data findings. All **46,642** JPEGs fully
decoded and were hashed; all **45,693** rectangle JSON files parsed. No missing expected or orphan
rectangle files, unreadable images, malformed point arrays, nonfinite/degenerate rectangles,
empty shapes or reference mismatches
were found. All 949 annotation-free images belong to the explicit non-threat source folder.
That folder declaration is not a model benign decision.

| Check | Train | Test |
|---|---:|---:|
| Decoded / hashed images | 30,044 / 30,044 | 16,598 / 16,598 |
| Parsed rectangle JSON files | 29,444 | 16,249 |
| Rectangle instances | 36,487 | 20,587 |
| JSON dimensions differ from JPEG | **29** | **10,920** |
| Within-split exact duplicate groups | **601** | **43** |
| Redundant image files in those groups | 601 | 43 |

There are **55 rectangles outside actual JPEG bounds**: 36 boxes in 19 train images and 19
boxes in 19 test images, listed in local `out-of-bounds-boxes.csv`. Their points satisfy the declared JSON
bounds, so trusting metadata alone would miss these failures. The audit does not rescale, clip,
rename, remove or rewrite source records. Data is **not cleared for conversion/training**.

The independent header/JSON pass agrees on all **10,949** dimension mismatches and lists every
affected record in `dimension-mismatches.csv`. Train has 29 distinct dimension deltas, affecting
24 multilabel, four cutter and one bullet images. Test has 4,916 distinct deltas: 4,291 cases
are exactly +1 width/+1 height, but 6,629 are different, including large differences. For example,
test Battery `2011-01-01-014922-1` declares 1440×960 for a 619×348 JPEG. A blanket metadata
overwrite or resize is not a justified correction. Whether some neighboring train filenames
have shifted pairings remains an **unverified hypothesis**, not a repair rule.

**No exact image-byte hashes overlap across train/test.** The 84 shared relative filenames are
all wrench images with different bytes. Include split in scan identity. All 644 within-split
duplicate groups contain two images; repeated filenames alone did not identify these groups.
No near-duplicate or physical-group independence claim follows from the hash check.

Raw annotation labels are 20 consistent strings across both splits, with no case/whitespace
variants. In particular, the `Injection` folder contains `Syringe`; `3D Gun` uses
`3D printed gun`. No integer IDs or folder-number mapping has been assigned.

| Raw label | Train instances | Test instances |
|---|---:|---:|
| Explosive | 2,758 | 3,733 |
| Gun | 4,702 | 561 |
| 3D printed gun | 2,125 | 1,204 |
| Knife | 3,386 | 564 |
| Cutter | 1,629 | 587 |
| Blade | 904 | 452 |
| Shaving Razor | 873 | 411 |
| Lighter | 840 | 1,186 |
| Syringe | 854 | 369 |
| Battery | 4,091 | 4,498 |
| Nail Cutter | 879 | 402 |
| Other Sharp Item | 880 | 672 |
| Powerbank | 1,037 | 515 |
| Scissors | 1,348 | 1,474 |
| Hammer | 1,606 | 669 |
| Pliers | 1,200 | 1,338 |
| Wrench | 2,121 | 506 |
| Screwdriver | 1,340 | 517 |
| Handcuffs | 863 | 365 |
| Bullet | 3,051 | 564 |

**Paper versus inspected release:** Figure 5 in the
[STING-BEE paper](https://arxiv.org/html/2504.02823v1#S3.F5) reports 36,487 train and 20,731
test instances. Local train totals match; local test has **144 fewer Battery annotations**
(4,498 versus the published 4,642). The other 19 test class totals match. The reason is
unresolved; do not invent missing boxes or report the paper total as the local count.

Visual review: six representative original/ground-truth pairs cover explosive, multilabel and
explicit non-threat examples in both splits. A seventh, large-mismatch training example
(`3DGun+Bullets2_B2_L1_C2_Loc2_phi2_th1_2`) visibly places raw annotation boxes beside the
baggage; declared 614×301 versus actual 964×510. Metadata-only correction would leave those
raw boxes displaced. Saved previews explicitly say ground truth/no model inference.

Software verification: `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest -q` passed **84 tests and 37 subtests** in 3.28 seconds.
The tests use synthetic software fixtures. Independent review reproduced a path escape through
a filesystem link, then verified the fix: linked/reparse entries are rejected before reads.
No unresolved blocking code finding remains from that bounded review. No model was loaded.

## Next actions

STCray is deferred while P1 uses IEDXray. If adopted later, resolve the listed image/annotation
geometry, Battery count and duplicate findings before conversion or training. No repeat access
request is needed for the supplied files. The primary IEDXray [generic forward pass](first-inference.md)
is now verified; its next steps are device inference and the agreed P1 pipeline. STCray ground-truth
previews remain data-inspection evidence, not model predictions.

## Remaining limits

Captions and mask/polygon semantics are not audited. Exact-byte checks cannot establish absence
of near duplicates, repeated physical objects or overlap with IEDXray/Falcon-X. No verified
physical-group metadata was supplied. Keep the published splits intact; investigate findings
before conversion or training. No model accuracy, benign decision or inference readiness is inferred.
