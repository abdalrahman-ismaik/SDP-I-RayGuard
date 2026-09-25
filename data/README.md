# External data

The user supplied local STCray archives and extracted IEDXray files; see the
[STCray audit](../docs/stcray-audit.md) and [IEDXray audit](../docs/iedxray-audit.md).
The [IEDXray Figshare record](https://doi.org/10.6084/m9.figshare.30784328) is the published
source, but its original ZIP checksum cannot be compared with the supplied extracted files alone.
The approximately 70K internal images are reported separately; their relationship is unresolved.
IEDXray is the current P1 dataset; STCray is optional and deferred.

The 24 September meeting separately requires a **distributed dismantled dataset**: all five
students repeat the same five-session weekly rota for two consecutive weeks, ten sessions
total, completed by **15 October 2026**. Exact lab slots, taxonomy, grouping and image quota
remain to be confirmed. Use the lab's protocol and record actual session/case/physical-instance
provenance and QC. The published datasets do not fulfil this new collection. A second two-week
batch after midterms, followed by retraining, is planned; exact dates are unassigned.

Keep data outside Git (or in this ignored directory). Set `dataset_root` and `annotations` in
`configs/project.local.json`, or shell `SDP_DATA_ROOT` / `SDP_ANNOTATIONS`. Layout is not assumed:
identify the actual image root and train/test JSON paths first. Preserve all published splits and
the four annotation groups (complete, devices, generic threats, specific threats) separately.

Inventory source/license/access owner, download date, file sizes/SHA-256, annotation task,
category IDs and names, image paths, split origin, scanner provenance and physical-group metadata.
Do not assume one host per image, one box per benign image, or host-region links. Empty annotations
are task-specific negatives, not proof an image is safe or annotations are complete.

Run the implemented audit with explicit paths and optional other split/image roots. Missing
roots/groups mean corresponding checks remain unverified. Check exact hashes where possible;
near duplicates and physical identity require further investigation. Do not repartition the test
set or treat filename grouping as authoritative. Real-image annotation previews were reviewed
during the audits. The [generic baseline runner](../scripts/infer_generic_yolov10.py) renders
model predictions; the audit CLI does not provide a general annotation-overlay command.

STCray uses `STCray_TrainSet` and `STCray_TestSet`, each containing `Images`, `Json_BB`,
`Json`, `Segmentation` and `Captions`. Run `audit-stcray data/STCray/extracted` using the
package CLI above. `Json_BB` contains per-image rectangle corners in original pixel coordinates,
not COCO `xywh` or the normalized coordinates used in some STING-BEE instruction outputs.
The audit reads source files without repairing them; inspect findings before conversion/training.
Caption contents, mask semantics, near duplicates and physical groups require separate checks.

IEDXray's actual roots are `data/IEDXray/Train`, `Test` and `annotations`. The ignored local
config now points to its generic train JSON. All four task image tables match; full image checks
were run through the complete pair. Device Mobile/Pager labels disagree between exports, four
image hashes cross splits and 13 distinct boxes violate strict bounds. Resolve these before
conversion/training or fair evaluation. Do not construct filenames from image IDs, relabel
Mobile/Pager globally, infer benign status from task-empty images, or silently change test data.
