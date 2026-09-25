# Research and artifact evidence

Updated **24 September 2026**. Paper and release observations below were made on
21–22 September; they are dated evidence, not a fresh check of moving upstream releases.
The supplied IEDXray paper and FALCON v2 were read completely. Page references use PDF
page numbers, including front matter.

## Scope and evidence

[Meeting 02 and its follow-up](meeting_minutes/README.md) prioritize the new distributed
dataset, existing-model adaptation and an early GUI/poster showcase. Published datasets and
models support that work; they do not supply the new lab taxonomy or cross-package ground truth.
The meeting's ready-model statement is documented availability, not verified GUI execution.
See [requirements and open questions](context.md) and the [current backlog](tasks.md).

| Evidence category | Meaning |
|---|---|
| Recorded requirement | An instruction in the meeting record, follow-up or project proposal |
| Paper finding | An author's reported method, dataset property or experimental result |
| Project recommendation | A proposed implementation or evaluation choice |
| Unresolved question | A dependency not established by the available evidence |

Implementation evidence is **documented** when described by a source, **artifact inspected**
when particular files or metadata were examined, and **executed and verified** when a real run
has saved evidence. A public file listing alone establishes neither file contents nor working inference.

## IEDXray: published evidence

Takele et al., [A Benchmark Dataset for Concealed Improvised Explosive Device Detection in
X-ray Security Imaging](https://doi.org/10.1038/s41597-026-07263-7), Scientific Data 13:962 (2026).

| Paper evidence | Project implication |
|---|---|
| PDF pp. 4–6, Fig. 3: 17,360 processed RGB images; 12,224 train / 5,136 test; eight COCO files in four annotation pairs. Raw dual-energy arrays are unavailable. | Inspect the actual task map and retain original image coordinates. The internal collection mentioned in the minutes is not established as this dataset. |
| PDF p. 5, Dataset Split Strategy: physical configurations and concealment setups are separated between train and test. | Preserve the published split. Verify supplied-file overlap and physical provenance separately. |
| PDF p. 7, Fig. 5: device, generic-explosive and specific-explosive detection are separately fine-tuned tasks; benign electronics are negatives for specific detection. | The benchmark does not itself implement the proposed sequential P1 pipeline, host-region association or benign decision policy. |
| PDF p. 6, Fig. 4, and p. 9, Fig. 6/limitations: class imbalance, clutter, small objects and occlusion; controlled acquisition on one scanner. | Examine per-class errors and false positives. Published performance does not establish cross-scanner or operational performance. |

Authors' reported results, PDF p. 7 Table 2 and p. 8 Tables 3–4:

| Model | Device AP / AR | Generic AP / AR | Specific AP / AR | Parameters | Device-table FPS |
|---|---:|---:|---:|---:|---:|
| YOLOv10-M | 67.0 / 70.8 | 35.1 / 48.4 | 36.8 / 49.0 | 16.5M | 77.0 |
| Grounding DINO | 69.0 / 71.9 | 48.9 / 57.2 | 43.5 / 47.5 | 172M | 8.4 |
| RTMDet | 61.3 / 92.2 | 28.9 / 61.1 | 29.0 / 61.0 | 24.7M | 28.5 |

AP is mAP@[.50:.95]; AR is average recall, not precision. The paper reports RTX 4090 24GB,
batch one and FP32 (PDF p. 6). These FPS figures are not full application latency.
Grounding DINO was fine-tuned; zero-shot use would be a different experiment.

## IEDXray: inspected artifacts and executed baseline

The [Figshare record](https://doi.org/10.6084/m9.figshare.30784328), inspected on 21–22 September,
lists a CC BY 4.0 dataset. The inspected [author source revision](https://github.com/Natnael-gh/IEDXray/tree/b4c32df0cd141d3d5f420dee9ff0ea135a036a85)
is not established as the checkpoints' training revision. The supplied files have local hashes;
publisher byte identity is unverified.

- **Executed data audit:** all 17,360 supplied images decode and match declared dimensions.
  Findings include four exact-byte train/test pairs, 4,955 same-box Mobile/Pager name
  disagreements between exports and 13 distinct boundary violations. Six complete modified-host
  images lack corresponding region boxes. No label correction or split modification was applied.
  [Audit details](iedxray-audit.md).
- **Paper cross-check:** Fig. 4's displayed aggregate class counts match the complete export.
  This supports those aggregate counts without establishing every label or an authoritative
  correction for the device export. Machine category IDs and training order are not specified
  by the figure. [Paper/annotation review](iedxray-paper-review.md).
- **Artifact inspected:** 18 checkpoints across six model families were hashed and passed
  archive CRC checks. Static metadata exposes several class/head/configuration issues; archive
  integrity does not prove semantic correctness. [Checkpoint catalog](checkpoint-catalog.md).
- **Executed inference:** the generic YOLOv10-M checkpoint runs on CPU with the
  [original THU-MIG source at 453c6e3](https://github.com/THU-MIG/yolov10/tree/453c6e38a51e9d1d5a2aa5fb7f1014a711913397),
  Python 3.11.9, PyTorch 2.9.0+cpu and torchvision 0.24.0+cpu. Three diagnostic images produced
  one detected training example, one missed annotated test threat and one empty ordinary-laptop
  result at confidence 0.25. The positive box/score repeated exactly.
  [Commands, predictions and limits](first-inference.md).

The embedded YOLO architecture and names are sufficient for the completed generic smoke run;
missing configuration sidecars no longer block that reference. Device execution, full P1
association/decision logic, fine-tuning and model evaluation remain unfinished. The other
checkpoint backends have not been executed. The model environment is separate from the locked
CPU audit environment and is not an exact reconstruction of the author's training environment.

**Recommendation:** retain the working YOLO reference and verify the intended device/demo
pairing next. Its published size/speed supports this practical starting point; it is not the
highest-AP model in the paper. A different verified lab model may be appropriate for the new
distributed task. Additional detector comparisons remain optional.

## FALCON: published scope and inspected release

Michael et al., [FALCON: Functional Assembly and Language for Compositional Reasoning in
X-ray](https://arxiv.org/abs/2606.25701v2), supplied v2 dated 29 June 2026.

| Paper finding | Limitation for this project |
|---|---|
| PDF pp. 4–8, §§3–5: single-image component presence, functional completeness and grounded reasoning | Does not supply cross-bag grouping or genuine distributed-case ground truth |
| PDF pp. 9–11, §6/Fig. 5: DINOv2, RF-DETR proposals/masks, structured adapter and Vicuna-7B; p. 10 distinguishes relational compatibility from physical connectivity | Component presence or a fluent explanation does not establish physical assembly or danger |
| PDF pp. 13–14, Tables 3–6: grounding/reasoning results and ablations | These metrics are not directly comparable with IEDXray box AP |
| PDF p. 6, §4.4, and pp. 18–22, §§9–10: base-image split keeps original/counterfactual variants together | Preserve variant provenance; synthetic regrouping validates software, not real multi-package detection |
| PDF pp. 24–25, §13/Table 10: three training stages on two A100 GPUs; p. 27, §15: multi-view/multi-context reasoning is future work | Full retraining is outside the current critical path; P2 needs its own cross-image method and evaluation |

Release inspection on **21 September 2026**:

| Pinned primary artifact | Observed state |
|---|---|
| [Code and package](https://github.com/yonathan-kiflom/FALCON/tree/bce31b7ea41264463db36fa185661732c2804c6f) | A demo is documented; Python 3.10–3.11 and model dependencies are specified. No local installation or execution was verified. |
| [Model card](https://huggingface.co/JonathanJMK/FALCON/blob/c64501338fd78b9132da6997b8e02e2003d40c65/README.md) | Describes Stage-3 weights, single-device loading and precision constraints. Llama 2 terms also apply; the code license does not establish one license for every component. |
| [Model configuration](https://huggingface.co/JonathanJMK/FALCON/blob/c64501338fd78b9132da6997b8e02e2003d40c65/config.json) | Three-category presence enabled; risk and three link heads disabled, with no recorded risk/link supervision. Detector resolution 768 differs from paper Table 10's 448; the release visual encoder uses 448. These are inspected differences, not runtime measurements. |
| [Evaluation documentation](https://github.com/yonathan-kiflom/FALCON/blob/bce31b7ea41264463db36fa185661732c2804c6f/docs/evaluation.md) | Labels/reductions differ from the archived paper; this is not exact numerical reproduction. Completeness measures category presence and expert risk/link labels are absent. Its 1,383 complete originals plus 8,298 incomplete variants give an always-incomplete baseline of 85.7%; balanced metrics matter. |
| [Model listing](https://huggingface.co/JonathanJMK/FALCON/tree/c64501338fd78b9132da6997b8e02e2003d40c65) | Public, ungated metadata; four shards total about 15.01 GB. Listing inspection does not verify downloads, loading or VRAM requirements. |
| [Dataset listing/card](https://huggingface.co/datasets/JonathanJMK/falcon-x/tree/7ca15293a551c94e1e65b249f7bcaea29e4b0312) | About 1.316 GB of listed archives; 6,911 originals and 41,454 counterfactuals. Paper prose rounds originals to 7,000; Table 1 gives 6,911. Archive contents were not inspected. |

**Recommendation:** keep FALCON as a bounded component-grounding research option after the
required collection and showcase work. The inspected release is narrower than the paper's
risk/link discussion and has not been run here. It is not a complete P2 implementation.

## Optional STCray evidence

The supplied STCray release was audited on **22 September**: 46,642 images decoded/hashed,
45,693 rectangle JSON files parsed, 10,949 dimension mismatches, 55 out-of-bounds boxes,
644 within-split exact duplicate pairs and no cross-split byte duplicates. Physical independence
remains unverified. The supplied test annotations contain 4,498 Battery instances versus 4,642
in STING-BEE Fig. 5; the difference is unresolved. [Full audit and sources](stcray-audit.md).

STCray remains optional and deferred for P1. Neither it nor IEDXray replaces the required new
distributed collection. The broader [dataset catalog](datasets.md) distinguishes original
releases, derivatives and datasets merely used by the authors.

## Evaluation implications

Preserve the published test split and original annotations. Resolve known semantic/overlap
findings before claiming a valid evaluation; document physical-group uncertainty. An author
checkpoint trained on all published training images has already seen a validation subset carved
from those images. Such a subset cannot establish unseen validation for that checkpoint.

Record task/category order, transforms and threshold choices. Freeze choices before final
test reporting. A crop cascade needs coordinate remapping, padding, multiple-host handling,
unmatched regions and stage-error analysis; full-image association is a separate design choice.
Neither is provided automatically by the benchmark. Empty detections imply no benign verdict.
See [architecture](architecture.md) and [verification](verification.md) for implementation limits.
