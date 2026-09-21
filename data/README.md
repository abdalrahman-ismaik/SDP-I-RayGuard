# External data

No real dataset has been inspected. Acquire only through authorized lab access or the
[IEDXray Figshare record](https://doi.org/10.6084/m9.figshare.30784328), after reviewing terms.
The approximately 70K internal images are reported separately; their relationship is unresolved.
No download is part of bootstrap.

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
set or treat filename grouping as authoritative. Overlays/manual real-image inspection are the
next data task; overlay generation is not implemented in bootstrap.
