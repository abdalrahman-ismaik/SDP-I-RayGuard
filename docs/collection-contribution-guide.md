# Distributed collection contribution guide for team members

Use this guide to make collection work verifiable for the individual GitHub assessment. It is a shared checklist for each member; fill only your own work, use actual evidence and ask the coordinator/lab about any protocol field that is not defined. This guide does not assign scans, approve labels or create physical groups.

## Keep X-ray files out of GitHub

The scans are already on the lab computer; keep that as the source location. No additional upload or transfer is needed. The shared repository is public and project rules exclude scans, filled schedules, personal/session records and restricted artifacts from commits. Do **not** add JPEGs, ZIPs, per-image scan logs, personal IDs, private paths or filled manifests to a commit or pull request. Do not make an extra copy in personal cloud storage or a public GitHub release.

Keep original image bytes unchanged. Do not crop, rename, rotate, recompress, annotate or delete the source copy. If the lab approves a canonical folder layout, retain the original archive separately and create a documented working copy. Do not remove duplicate copies until the data owner approves the canonicalization.

## Each member's individual contribution

Complete these steps for scans you personally collected or handled:

1. **Confirm ownership and scope.** Privately confirm your name and GitHub username with the coordinator. State which collection round/session and date range you personally attended. Do not claim images from another member's folder.
2. **Inventory your files privately.** Count original files and exact duplicate payloads separately. Record filename-date counts, file types, byte sizes, SHA-256 hashes, dimensions, decode failures and inventory command/tool version in a private manifest. Filename dates are not confirmed scanner timestamps.
3. **Record approved provenance.** Use only lab-approved values for collector code, session, scanner/export source, bag slot, case/group/physical-instance identity and configuration. Record unknown values as unknown. Never invent category IDs, case IDs, groups, benign labels or outcomes from an empty detection.
4. **Record QC separately.** Track review status, rejection/rescan reason and reviewer in the private manifest. Separate acquired, distinct-file, reviewed/usable, rejected and pending counts. A decodable image is not automatically an accepted scan.
5. **Verify in place.** Work from the existing lab-computer copy. Do not transfer or duplicate the scans. If the lab has multiple working folders, ask the data owner which is canonical; verify the selected copy by file count and SHA-256 without modifying it. Keep the filled per-image manifest and any local paths on the lab computer/private storage.
6. **Create your own GitHub evidence.** Open a branch/PR with a concise sanitized contribution note: dates, verified aggregate counts, files/docs/code authored, what you reviewed, commands/results, limitations and links to issues/PRs/commits. Do not include images, per-image hashes, IDs, local paths, private links or attendance receipts.
7. **Review and explain.** Request an independent review of your inventory summary and explain your method and contribution to the supervisor. Record reviewer/date in the shared note only after it happens.

## What to commit

Use your own PR and meaningful commits. Suitable shared work includes a sanitized contribution note; a correction to the [collection inventory](collection-progress-2026-11-14.md) after verification; improvements to the blank [collection manifest](templates/collection-manifest.csv), instructions or audit code; a protocol/QC decision note after lab confirmation; or reproducible audit code with the required checks for code changes.

Do not create a commit solely to inflate activity. Each contributor must be able to explain the actual work and evidence. The GitHub record is one part of individual assessment, not proof that a collection count was accepted by the lab.

## Sanitized contribution note template

Copy this structure into a Markdown file in your PR. Replace every prompt with verified facts or `not verified`; remove fields that disclose restricted information.

```markdown
# Collection contribution — [name] — [round/date]

- Contributor / GitHub username:
- Work personally performed:
- Collection dates (source of date):
- Acquired image files:
- Exact duplicate file paths excluded from distinct-file count:
- Distinct byte payloads:
- QC accepted / rejected / pending (reviewer and date):
- Private manifest/source copy verified in place by:
- Commands/tool version and result:
- Shared files/code authored or reviewed (PR/commit links):
- Limitations or unresolved lab decisions:
- Supervisor explain-back (date/reviewer; fill only after it occurs):
```

Public contribution notes contain aggregate counts only. Keep filled per-image manifests, hashes, paths, scanner metadata and identifying case maps with the lab-computer source or other approved private records; do not transfer scans.

## Team reconciliation

The current lab-computer inventory reports 577 image paths and 478 distinct byte payloads, including 99 exact copies in one `total` folder. This is a provisional inventory, not an accepted/usable count or verified round mapping. Each member should verify only their own contribution on the lab computer. The coordinator should reconcile the private manifests against the lab's approved catalogue and QC log before changing the shared total. See [the dated inventory](collection-progress-2026-11-14.md) and backlog T21/T27.
