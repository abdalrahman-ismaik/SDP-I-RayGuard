# Dataset catalog and RayGuard suitability

Checked **22 September 2026**. This catalog covers datasets introduced or curated by the
Khalifa group or coauthored by Naoufel Werghi / Divya Velayudhan that could be verified from
primary public sources. It is a dated discovery inventory, not a guarantee of every historical
lab dataset. Public, gated, announced and paper-only collections are distinguished below.

The [CVML-KU GitHub profile](https://github.com/CVML-KU) identifies Werghi's Computer Vision
and Machine Intelligence Lab and links its projects. Its repository collection is a showcase,
not a complete dataset index. The [KU publication profile](https://khazna.ku.ac.ae/en/persons/naoufel-werghi-7/)
and [author website](https://naoufelwerghi.com/) provide broader discovery. Other organizations
named CVMI (including HKU's CVMI-Lab) are not this Khalifa lab.

Evidence level: paper descriptions are **documented**; release cards, file listings and API
metadata below were **artifact inspected**. This survey did not download archives, accept access
terms, validate image/annotation contents or execute models.

**Project artifact status:** the available STCray base archives were inspected separately.
See the [executed local audit](stcray-audit.md) for provenance, counts, format and findings.
The public release remains gated; each user must follow its access conditions. An unavailable
Hugging Face dataset viewer does not by itself indicate an access denial.

## Directly relevant X-ray datasets

| Dataset / authorship | Contents and task | Access observed | RayGuard recommendation |
|---|---|---|---|
| **IEDXray (2026)**; Takele et al., including Velayudhan and Werghi | 17,360 processed RGB scans; published 12,224 train / 5,136 test; device, generic-threat and specific-threat detection; four annotation groups | [Figshare](https://figshare.com/articles/dataset/IEDXray_Dataset/30784328) publicly lists one 482,371,434-byte ZIP under **CC BY 4.0**. [Paper](https://doi.org/10.1038/s41597-026-07263-7) identifies it as the public release | **Primary P1 dataset.** Download/audit can proceed from the published source when acquisition is undertaken; a private lab copy is not a prerequisite. Preserve published splits |
| **STCray (2025)**; STING-BEE, Velayudhan et al., including Werghi | 46,642 scans, 30,044 train / 16,598 test; boxes, masks, classifications and captions; broad prohibited-item detection including explosive examples | [Author release](https://huggingface.co/datasets/Naoufel555/STCray-Dataset) labels **Apache-2.0** and is gated. Base train/test archives total 2,074,502,418 bytes; separate augmented archive is 21,549,496,513 bytes | Useful secondary detector/segmentation/VLM dataset. Its explosive class does not automatically provide IEDXray's modified-device task labels. Inspect real mappings before reuse |
| **Falcon-X (2026)**; Michael et al., including Werghi (Divya is not in the cited author list) | Release card lists 6,911 original scans plus 41,454 edited counterfactual images; component boxes/masks and language tasks for battery, detonator and explosive | [Public Hugging Face files/card](https://huggingface.co/datasets/JonathanJMK/falcon-x); API says ungated. Train/test archives about 1.316 GB. No explicit dataset license in inspected card/metadata; resolve terms before adoption | Component-grounding candidate for P2 research. Single-image category presence does not provide multi-bag case ground truth or verified functional links |
| **StingBee_XrayInstruct (2025)**; STING-BEE authors | Instruction/answer annotations derived from STCray images; a language-data layer rather than a separate scan acquisition | [Hugging Face release](https://huggingface.co/datasets/Divs1159/StingBee_XrayInstruct) is ungated and labeled Apache-2.0; JSON listed at 138,590,321 bytes | Optional VLM work, not needed for first detector inference; source images still follow STCray access conditions |
| **STING-BEE VQA benchmark (2025)**; STING-BEE authors | Paper reports 39,194 questions over STCray test, SIXray and PIDray images; adds evaluation questions to existing scans | [Release directory](https://github.com/Divs1159/STING-BEE/tree/main/stingbee/eval/VQA%20Evaluation%20Benchmark) contains three question JSONLs and three answer XLSX files; annotation license not established | Derived evaluation resource; source-image access/terms remain separate. Reported per-dataset counts sum to 39,195, so exact total needs file audit |
| **GDXray / SIXray mask annotation releases (CIE-Net, 2021/2022)**; Hassan et al., including Werghi | Additional manually drawn segmentation masks for existing GDXray and SIXray scans; GDXray annotation work includes a chip category | [Author repository](https://github.com/taimurhassan/inc-inst-seg) and its `dataset details.pdf` link two annotation ZIPs on Drive. Download not tested; no dataset license established | Annotation derivatives, not new lab-acquired scan collections; source-image access/terms remain separate |

STCray naming/count nuance: the [project page](https://divs1159.github.io/STING-BEE/) advertises
21 categories but its statistics specify 20 threat categories; the non-threat class explains
the overall classification count. Confirm the actual annotation namespace before converting.
The Hugging Face card's `100M<n<1B` size tag conflicts with its documented 46,642 images; do
not treat that metadata tag as the image count. The listed 23.6 GB total includes augmentation;
the base train/test files are much smaller. The initial survey did not inspect archives; the
subsequent [local audit](stcray-audit.md) examines the user-supplied base release.
The [STING-BEE paper](https://arxiv.org/html/2504.02823v1), section 4.3 and Appendix E,
describes a separate synthetic augmentation derivative (approximately 25,000 images); do not
count it as an independent acquisition of real scans.

Falcon-X release metadata is pinned at `7ca15293a551c94e1e65b249f7bcaea29e4b0312` for this
observation. Its `dataset.json` defines functional completeness as the presence of all three
categories. The [released evaluation documentation](https://github.com/yonathan-kiflom/FALCON/blob/bce31b7ea41264463db36fa185661732c2804c6f/docs/evaluation.md)
explicitly distinguishes available labels from the paper. Keep base images and counterfactuals
together across splits. Model execution and compatibility with this project remain unverified.

## Other domains: verified introduced or curated datasets

These are author collaborations; inclusion does not imply every dataset originated entirely
inside one lab. Counts are release/paper claims, not counts from local archive inspection.

| Dataset / publication | Domain and scope | Attribution | Observed access / terms |
|---|---|---|---|
| **AD / Abu Dhabi Greenhouse Tomato Leaf Dataset (2026)** | 502 images, four leaf-health classes; newly collected greenhouse images | Shafay et al., including Divya and Werghi; [author repository](https://github.com/mshafay5/DLCAF-LLM) | [Figshare](https://doi.org/10.6084/m9.figshare.31145998), current v2; public file listing, CC BY 4.0 |
| **HBID24K (deposit 2025, paper 2026)** | 24,318 camera-trap images; Houbara/intruders, 21 wildlife classes and boxes | Ali et al., including Werghi; [paper](https://www.nature.com/articles/s41597-025-06496-2) | [Figshare](https://doi.org/10.6084/m9.figshare.28202888.v1); public listing, CC BY 4.0; full split archives about 12.1 GB and separate 2,027-image sample |
| **HBCE (2025)** | 10,394 images, 23,387 instances; Houbara adult/chick/egg labels | Ali et al., including Werghi; [official repository](https://github.com/sadaf-ali/HBCE) | Dataset/code by email request per README; no public archive or data license found. Overlap with HBID24K unresolved |
| **D-PTUAC (deposit 2023, paper 2024)** | Drone person tracking in uniform-appearance crowds; 138 sequences, over 121,000 frames | Alansari et al., including Werghi; [project](https://d-ptuac.github.io/), [paper](https://www.nature.com/articles/s41597-023-02810-y) | Public CC BY 4.0 [RGB release](https://doi.org/10.6084/m9.figshare.24590568.v2) (~16.1 GB), [earlier RGB/depth-linked release](https://doi.org/10.6084/m9.figshare.24081597.v1) (~21.5 GB). Variants of one dataset |
| **PTUA / earlier PTUG (deposit 2022, paper 2023)** | Robot-mounted RGB-D person tracking; paper reports 45 sequences, over 85,000 frames | Zhang et al., including Werghi; [KU publication](https://khazna.ku.ac.ae/en/publications/robot-person-tracking-in-uniform-appearance-scenarios-a-new-datas/) | [Project](https://ptug.github.io/) and [Zenodo](https://zenodo.org/records/6915133): public, CC BY 4.0, about 20.1 GB. Naming/version correspondence needs care; 48 ZIP files are not proof of 48 sequences |
| **UTB180 (2022)** | 180 underwater tracking sequences, over 58,000 annotated frames; collected and online-source video | Alawode et al., including Werghi; [author repository](https://github.com/BasitAlawode/UTB180) | [Kaggle release](https://www.kaggle.com/datasets/bastech/utb180) lists about 12.1 GB, CC0. Actual download/login behavior untested |
| **UVOT400 (release/preprint 2023; journal 2026)** | 400 underwater tracking sequences, 275,000 frames, 17 attributes; language descriptions added 2026 | Werghi coauthors the [2023 preprint](https://arxiv.org/abs/2308.15816); the current journal citation has a different author list | [Official repository](https://github.com/BasitAlawode/UVOT400) links train/full-test files and language descriptions. Repository MIT license does not establish image-data licensing |
| **EMT / Emirates Multi-Task (2025)** | Gulf-region driving; 34,386 frames, 57 minutes; tracking, trajectory/intention prediction | Abdel Madjid et al., including Werghi; KU AV Lab collaboration; [paper](https://arxiv.org/abs/2502.19260) | [Hugging Face](https://huggingface.co/datasets/KuAvLab/EMT): public listing, CC BY-NC-SA 4.0, 30.6 GB. [Repository](https://github.com/AV-Lab/emt-dataset) conflicts on total boxes (626,634 versus 576,374); unresolved |
| **Labeled Facets / Labeled 3D Texture Dataset (2022)** | Facet annotations/geometric attributes derived from SHREC'18 and Real-World Textured Things meshes | Ganapathi and Werghi; [publisher record](https://diglib.eg.org/items/32385388-32d4-4d3a-972d-cf26cb8743bf), [DOI](https://doi.org/10.2312/3dor.20221181) | Author download redirects to an expired KU SharePoint link. Count and dataset license not established; source meshes are third-party |

## Published/announced work without a verified downloadable dataset

| Collection | Published content and authorship | Current limit |
|---|---|---|
| **DebrisVision (ICCV workshop 2025)** | Compiled/augmented underwater debris benchmark; 9,430 real + 15,570 synthetic images, 24 classes, boxes/masks/estimated depth/text. Divya and Werghi coauthor the [project](https://eswarmachara.github.io/research/debrisvision) | [Repository](https://github.com/EswarMachara/DebrisVision) explicitly says dataset link coming soon. Its MIT code license does not establish rights to aggregated source images |
| **Cytoplasmic Strings / CS_Detection (2025)** | New embryo annotations derived from third-party Gomez et al. videos: 90 sequences, 13,568 frames, 271 positives; Divya and Werghi coauthors. [Paper](https://arxiv.org/html/2512.09461v1) | [Repository](https://github.com/HamadYA/CS_Detection) explicitly excludes data. Data release promised; license unverified |
| **Flare combustion-efficiency collection (September 2026 preprint)** | Custom synchronized RGB/IR/thermal video, gas-analyzer efficiency labels and wind metadata; Divya and Werghi coauthors. [Paper](https://arxiv.org/abs/2609.11262) | No dataset name, total size, public download or data license located |

## Exclusions and completeness limits

- SIXray, PIDray, GDXray, OPIXray, HiXray and COMPASS-XP are external scan datasets used in
  this group's work. Count explicitly released derivative annotations separately.
- **XSeg / AP-SAM** is external work by Gao et al.; no Divya/Werghi authorship in the
  [paper](https://arxiv.org/abs/2604.03706). It was a possible research lead, not a lab release.
- FieldPlant, PlantVillage, PlantDoc and Taiwan Tomato Leaf Disease are external benchmarks
  used in the [tomato project](https://github.com/mshafay5/DLCAF-LLM); AD is its newly collected dataset.
- For [SHREC'25 Multiple Relief Patterns](https://sites.google.com/unifi.it/shrec25-relief-pattern),
  KU contributed the KU-3DSeg method; Florence/TII organized the benchmark. The
  [report](https://arxiv.org/html/2508.09909v1) coauthorship is not evidence of lab ownership.
- [Person Monitoring by Full Body Tracking in Uniform Crowd Environment (2022)](https://arxiv.org/abs/2209.01274)
  describes a four-scenario annotated collection. Its separate name/release and relationship
  to PTUG/PTUA were not established, so it is not counted again.
- Older medical/face studies describe small experimental collections, but no independently
  verified public dataset release was established in this search. An author publication list
  can be broader than the publicly obtainable datasets; ask the group for its own inventory
  to establish completeness, private releases and relationships among overlapping collections.

## Availability and the next project action

**Current working choice: IEDXray only for P1.** STCray is an optional later resource for
broader threat categories, segmentation or vision-language experiments; its correction work is
deferred. No recorded advisor requirement makes it a prerequisite. The two local datasets share
some images, so a future external-evaluation or combined-training claim requires an overlap audit.
Neither supplies verified multi-bag case/group ground truth for P2.

**Recorded direction:** start with IEDXray/available old-scanner data (minutes PDF p. 5).
**Local update:** IEDXray has now been supplied extracted and [audited](iedxray-audit.md).
Its source identity is locally hashed; the original ZIP was not supplied. If available, preserve
that ZIP and compare its published MD5
`45962e6c4cf2a7acd0d637943f160f58` and calculate a local SHA-256. The extracted annotations
have already been audited. The public [Figshare API record](https://api.figshare.com/v2/articles/30784328)
was fetched without credentials. A listing/checksum is not proof the local extracted files match
the archive. Resolve the observed label/split issues before training or accuracy evaluation.

Dataset availability and pretrained-model availability are separate. The supplied IEDXray
weights now have an [inspected catalog](checkpoint-catalog.md) covering 18 checkpoints.
The generic YOLOv10-M pairing has produced [real CPU predictions](first-inference.md);
the device and specific-threat YOLO tasks have static metadata inspection only.
Physical-configuration metadata, internal collections and dataset overlap remain separate issues.
Two sampled non-threat scans are now verified byte-identical between local IEDXray and STCray;
full overlap remains unmeasured. Different dataset names do not establish independence.

The [STING-BEE repository](https://github.com/Divs1159/STING-BEE) separately links
`Divs1159/stingbee-7b` weights, code and a demo. These are distinct from the IEDXray detectors.
The README's two A100 80 GB GPUs describe its training setup, not a verified minimum for
inference. No STING-BEE installation or inference has been tested on the local RTX 2060.

A published dataset supports training and evaluation; immediate meaningful inference still
requires a task-trained checkpoint or a completed training run. The catalog survey, subsequent
dataset audits and generic-detector inference are separate evidence records; STING-BEE
inference remains unverified.

Using published data does not by itself resolve the proposal's separate 500-sample collection
or GUI timing questions. Those remain in the advisor log; no requirement is silently removed.
