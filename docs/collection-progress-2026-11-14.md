# Distributed X-ray collection inventory as of 14 November 2026

This is a repository-safe inventory of the collection snapshots on the lab computer. It counts JPEG files and exact byte duplicates; it does not certify annotation quality, scan usability, physical independence, case/group labels, lab acceptance or completion of the agreed collection protocol. Dates below are parsed from filename prefixes (`YYYYMMDD`), not verified scanner timestamps. Student labels come from source folder names; student IDs and local paths are omitted. The scans remain on the lab computer; this inventory does not call for uploading or transferring them.

## Latest snapshot

The extracted `DISMANTLE_DATA` tree contains **577 JPEG paths**. All 577 decoded successfully as RGB with Pillow. SHA-256 comparison found **478 distinct byte payloads**, so 99 paths are exact duplicate copies. The duplicate copies are in Ahmed Almansoori's `total` folder and match images also stored under bag folders. These are storage copies, not additional distinct image files. Byte-distinct files are not necessarily distinct physical scans or cases.

| Student folder label | JPEG paths | Distinct byte payloads | Exact-copy paths | Filename-date counts for distinct payloads |
|---|---:|---:|---:|---|
| Abd Alrahman Ismaik | 142 | 142 | 0 | 30 Sep: 92; 5 Oct: 34; 9 Oct: 16 |
| Ahmed Almansoori | 199 | 100 | 99 | 29 Sep: 24; 6 Oct: 41; 9 Oct: 35 |
| Ali Arif Alshamsi | 61 | 61 | 0 | 30 Sep: 21; 1 Oct: 16; 9 Oct: 24 |
| Faisal Daoud Alzarooni | 124 | 124 | 0 | 1 Oct: 72; 8 Oct: 52 |
| Mohammad Arwani | 51 | 51 | 0 | 29 Sep: 32; 6 Oct: 19 |
| **Total** | **577** | **478** | **99** | **22 below the planned 500 by distinct-file count** |

The 500 comparison is provisional. It does not determine whether the target means acquired files, accepted scans or catalogue rows for these artifacts. The remaining 22 cannot be treated as a confirmed collection shortfall until the lab confirms the mapping and the team reconciles the inventory against the approved catalogue/session log. QC may reduce the usable count.

## Distinct-file counts by filename date

Weekday labels use the 2026 calendar. These are filename-date buckets, not proof of attendance or booked session dates.

| Filename date | Day | Distinct byte payloads |
|---|---|---:|
| 29 Sep 2026 | Tuesday | 56 |
| 30 Sep 2026 | Wednesday | 113 |
| 1 Oct 2026 | Thursday | 88 |
| 5 Oct 2026 | Monday | 34 |
| 6 Oct 2026 | Tuesday | 60 |
| 8 Oct 2026 | Thursday | 52 |
| 9 Oct 2026 | Friday | 75 |
| **Total** |  | **478** |

## Archive snapshots

The dated archives have cumulative image-path counts; do not add them together.

| Archive label | JPEG entries | What the inventory establishes |
|---|---:|---|
| `DISMANTLE_DATA-30-09-2026.zip` | 169 | Snapshot content count only |
| `DISMANTLE_DATA-01-10-2026.zip` | 199 | Snapshot content count only |
| `DISMANTLE_DATA-05-10-2026.zip` | 291 | Snapshot content count only |
| `DISMANTLE_DATA-09-10-2026.zip` | 478 | 478 distinct byte payloads; Ahmed's files are at the student-folder root |
| `DISMANTLE_DATA-13-10-2026.zip` | 577 | Same 478 distinct byte payloads; Ahmed's 100 root-level paths were reorganized into bag folders and 99 exact copies appear under `total` |
| `DISMANTLE_DATA.zip` | 577 | Same 577 image paths as the 13 Oct archive; ZIP hashes differ |

The first four dated archives (30 Sep, 1 Oct, 5 Oct, 9 Oct) are nested path snapshots. From 9 Oct to 13 Oct, **100 Ahmed paths were moved** from the student-folder root into bag folders and 99 exact-copy paths were added under `total`; it is not a strict path superset. SHA-256 comparison confirms the 9 Oct and 13 Oct archives contain the same 478 distinct byte payloads, with no new or missing image payloads. The unlabelled archive has the same image paths as 13 Oct and a different ZIP hash. Do not sum archive counts.

The filename dates span **29 September–9 October**; archive labels are packaging/snapshot dates, not evidence that scans were collected on those dates. The files do not establish which scheduled round/session each belongs to.

## Audit performed and limits

- Read archive directory entries and counted image extensions without changing the archives.
- Counted extracted student folders, grouped by filename date, and compared SHA-256 values across all 577 files. Exact duplicates were found only in Ahmed's `total` copies.
- Decoded every JPEG with the locked project Pillow environment: 577/577 decoded, 0 errors, RGB mode. Dimensions vary across 408 distinct width/height pairs.
- Compared the 13 Oct and unlabelled archive image paths: both contain the same 577 paths. Their ZIP SHA-256 values differ.
- No annotation files, signed attendance, scanner/export log, approved group map, QC/rejection/rescan log or lab acceptance accompanied these files. No inference, training or category assignment was performed.

## Required next reconciliation

1. Ask the lab to confirm which folders/files belong to Round 1 and how these map to the approved 500-row catalogue.
2. Have each student confirm their own count and session/date interpretation; folder ownership is not proof of QC or individual authorship of later project work.
3. Identify the duplicate `total` folder as a mirror/export convention and ask the data owner which lab-computer copy is canonical. Preserve originals until the data owner approves cleanup.
4. Record approved case/physical-instance provenance and QC status in the private manifest. Do not infer groups from filenames or folder order.
5. Reconcile accepted/usable count and any shortfall with Dr. Divya before moving to the next round. F06's overall collection deadline remains 30 November 2026.

See the [member contribution guide](collection-contribution-guide.md). Raw X-ray files stay on the lab computer and per-image manifests remain private; neither belongs in Git.
