# IEDXray paper check — 22 September 2026

Re-read all 11 pages of the supplied benchmark PDF; rendered and visually inspected pp. 5–7.
This review separates published answers from discrepancies in the supplied local files.
It corrects the earlier suggestion that every audit finding needs advisor clarification before
the first generic-threat forward pass. See [audit evidence](iedxray-audit.md).

| Question | Answer already in the paper | Remaining local issue |
|---|---|---|
| Which task/annotation files? | Pp. 5, 7 / Figs. 3, 5: complete annotations plus three independently benchmarked tasks: device, generic explosive, specific explosive. | Actual source IDs come from each JSON; they do not establish a checkpoint's output order. |
| How many classes and what are negatives? | P. 7: four device types, one generic explosive class, five specific explosive types; benign electronics are negative examples for specific detection. | Six complete modified-host images lack threat boxes. Empty detector output is not evidence of a benign scan. |
| Intended split? | P. 5: physical IED configuration and concealment setup separated between train/test; p. 6: 12,224 / 5,136 images. | Four byte-identical image pairs cross the supplied split. Physical group IDs are absent locally. |
| Does the paper help choose the label export? | Fig. 4, p. 6: all 20 displayed counts (10 categories, two splits) match complete annotations. | Strong aggregate support for complete; not proof of every label. The paper does not explain the 4,955 same-box Mobile/Pager disagreements or give a correction map. |
| Which model/setup? | P. 6: YOLOv10-M, mostly MMDetection for other models; RTX 4090 24 GB, FP32, batch-one FPS. | Generic YOLO pairing and CPU execution are now verified; other task execution is pending. Paper hardware is not a local minimum requirement. |
| Where are data and weights? | P. 10: Figshare data and author GitHub repository. | The initial model link expired; the author renewed access and local weights were supplied. See the [checkpoint catalog](checkpoint-catalog.md). |

Figure 4 omits the complete export's `Modified parts` category. Its visual class ordering is
not a numeric category-ID or model-output-order specification. No global Mobile/Pager swap
is justified: the disagreement is not uniform across examples or splits.

Concrete examples, rechecked directly against source files:

- `Train000001.jpg`, image/annotation ID 1: complete category 6 `Modified Pager` versus device
  category 2 `Mobile`, at identical COCO box
  `[340.2124375, 138.8454305, 109.95861500000001, 66.57307300000001]`.
- `Train005219.jpg` and `Test001859.jpg` are byte-identical, SHA-256
  `13f4403b9dfab712f330a1de253fb1e60f050d81b42cef283932244ef1d6df25`.
  All four previously recorded cross-split pairs were rehashed and still match.
- Eleven tiny boundary excursions below 0.0003 pixels are a separate numerical issue;
  they should not be presented as equivalent in severity to conflicting class names.

Local evidence image: `runs/iedxray-audit-2026-09-22/paper-review-evidence.png`, with
`paper-review-evidence.json` and reproducible `render_paper_evidence.py`. These show source
annotations and images, not predictions. Source files/splits remain unchanged. The original
archive is absent, so these findings have not established a defect in every published copy.

**Next-action distinction:** [generic inference](first-inference.md) has since been verified.
Resolving device-label conflicts, evaluation overlap and validation provenance is separate work
before dependent training/evaluation claims; it does not block a technical device forward pass.

Primary sources: [benchmark paper](https://doi.org/10.1038/s41597-026-07263-7) and
[author repository](https://github.com/Natnael-gh/IEDXray/tree/b4c32df0cd141d3d5f420dee9ff0ea135a036a85).
