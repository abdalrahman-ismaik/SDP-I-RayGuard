# Apply the report layout to the Pandoc Word file with Microsoft Word (COM).
# Called by build-docx.ps1; needs Word installed. Sets A4, 25 mm margins,
# Times New Roman 12 pt with 1.5 spacing, booktabs-like table rules, the title
# page, and the contents / figure / table lists (from the markers docx_prep.py
# writes). Optionally exports a PDF for checking.
param([string]$In, [string]$Out, [string]$Pdf)
$ErrorActionPreference = 'Stop'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
  $doc = $word.Documents.Open($In)
  $mm = 2.8346
  $ps = $doc.PageSetup
  $ps.PaperSize = 7  # A4
  $ps.TopMargin = 25*$mm; $ps.BottomMargin = 25*$mm; $ps.LeftMargin = 25*$mm; $ps.RightMargin = 25*$mm

  $body = @('Normal','Body Text','First Paragraph','Compact','Bibliography','Block Text')
  foreach ($n in $body) {
    try { $s = $doc.Styles.Item($n) } catch { continue }
    $s.Font.Name = 'Times New Roman'; $s.Font.Size = 12
    $s.ParagraphFormat.LineSpacingRule = 1  # 1.5 lines
    $s.ParagraphFormat.SpaceAfter = 6; $s.ParagraphFormat.SpaceBefore = 0
    $s.ParagraphFormat.Alignment = 3  # justify
  }
  try { $c = $doc.Styles.Item('Compact'); $c.ParagraphFormat.SpaceAfter = 0 } catch {}
  $sizes = @{ 'Heading 1' = 20; 'Heading 2' = 15; 'Heading 3' = 13 }
  foreach ($n in $sizes.Keys) {
    $s = $doc.Styles.Item($n)
    $s.Font.Name = 'Times New Roman'; $s.Font.Size = $sizes[$n]; $s.Font.Bold = $true
    $s.Font.Color = 0; $s.Font.Italic = $false
    $s.ParagraphFormat.SpaceBefore = 12; $s.ParagraphFormat.SpaceAfter = 8
    $s.ParagraphFormat.KeepWithNext = $true
  }
  $doc.Styles.Item('Heading 1').ParagraphFormat.PageBreakBefore = $true
  foreach ($n in @('Table Caption','Image Caption','Caption')) {
    try { $s = $doc.Styles.Item($n) } catch { continue }
    $s.Font.Name = 'Times New Roman'; $s.Font.Size = 11; $s.Font.Italic = $false; $s.Font.Color = 0
    $s.ParagraphFormat.Alignment = 1; $s.ParagraphFormat.SpaceAfter = 8; $s.ParagraphFormat.LineSpacingRule = 0
  }
  try { $doc.Styles.Item('Table Caption').ParagraphFormat.KeepWithNext = $true } catch {}
  try { $doc.Styles.Item('Captioned Figure').ParagraphFormat.Alignment = 1 } catch {}

  # Tables: booktabs-like rules, small font, repeat header, fit to page.
  foreach ($t in $doc.Tables) {
    $t.Borders.Enable = $false
    $t.Range.Font.Size = 10
    $t.Range.ParagraphFormat.LineSpacingRule = 0
    $t.Range.ParagraphFormat.SpaceAfter = 2; $t.Range.ParagraphFormat.SpaceBefore = 2
    $t.Range.ParagraphFormat.Alignment = 0
    $t.Rows.AllowBreakAcrossPages = $true
    $t.TopPadding = 2; $t.BottomPadding = 2; $t.LeftPadding = 4; $t.RightPadding = 4
    $t.PreferredWidthType = 2; $t.PreferredWidth = 100
    $t.Borders.Item(-1).LineStyle = 1; $t.Borders.Item(-1).LineWidth = 12   # top
    $t.Borders.Item(-3).LineStyle = 1; $t.Borders.Item(-3).LineWidth = 12   # bottom
    $hdr = $t.Rows.Item(1)
    $hdr.HeadingFormat = $true
    $hdr.Range.Font.Bold = $true
    $hdr.Borders.Item(-3).LineStyle = 1; $hdr.Borders.Item(-3).LineWidth = 6
  }

  # Title page (text comes from docx_prep.py between the two markers).
  $r = $doc.Content
  $f = $r.Find
  if ($f.Execute('TITLEPAGE-START')) {
    $start = $r.Paragraphs.Item(1)
    $r2 = $doc.Content; $null = $r2.Find.Execute('TITLEPAGE-END')
    $tp = $doc.Range($start.Range.Start, $r2.Paragraphs.Item(1).Range.End)
    $tp.ParagraphFormat.Alignment = 1
    $tp.ParagraphFormat.SpaceAfter = 4
    $tp.Font.Size = 14
    foreach ($p in $tp.Paragraphs) {
      $txt = $p.Range.Text.Trim()
      if ($txt -eq 'Khalifa University of Science and Technology') { $p.Range.Font.Size = 16; $p.Range.Font.Bold = $true }
      if ($txt -eq 'TITLE-RAYGUARD') { $p.SpaceBefore = 36 }
      if ($txt -eq 'AI-Powered Explosive Detection in X-ray Scans') { $p.Range.Font.Size = 20; $p.SpaceAfter = 24 }
      if ($txt -eq 'Senior Design Project I') { $p.Range.Font.Size = 16 }
      if ($txt -eq 'Final Report') { $p.SpaceAfter = 24 }
      if ($txt -eq 'Team Members' -or $txt -eq 'Supervisor') { $p.Range.Font.Bold = $true; $p.SpaceBefore = 10 }
      if ($txt -like 'Fall 2026*') { $p.SpaceBefore = 36 }
    }
    $null = $doc.Content.Find.Execute('TITLE-RAYGUARD', $true, $false, $false, $false, $false, $true, 0, $false, 'RayGuard', 1)
    $rg = $doc.Content; $null = $rg.Find.Execute('RayGuard'); $rg.Font.Size = 32; $rg.Font.Bold = $true
    foreach ($m in @('TITLEPAGE-END','TITLEPAGE-START')) {
      $null = $doc.Content.Find.Execute($m, $false, $false, $false, $false, $false, $true, 0, $false, '', 2)
    }
  }

  function Replace-Placeholder($doc, $text, $title, $code) {
    $r = $doc.Content
    if (-not $r.Find.Execute($text)) { return }
    $r.Text = $title
    $r.Style = $doc.Styles.Item('Normal')
    $r.Font.Size = 20; $r.Font.Bold = $true
    $r.ParagraphFormat.Alignment = 0
    $r.ParagraphFormat.PageBreakBefore = $true
    $r.ParagraphFormat.SpaceAfter = 12
    $r.InsertParagraphAfter()
    $tgt = $doc.Range($r.End, $r.End)
    $tgt.ParagraphFormat.PageBreakBefore = $false
    $tgt.Font.Size = 12; $tgt.Font.Bold = $false
    $null = $doc.Fields.Add($tgt, -1, $code, $false)
  }
  Replace-Placeholder $doc 'TOC-PLACEHOLDER' 'Contents' 'TOC \o "1-3" \h \z \u'
  Replace-Placeholder $doc 'LOF-PLACEHOLDER' 'List of Figures' 'TOC \h \z \t "Image Caption,1"'
  Replace-Placeholder $doc 'LOT-PLACEHOLDER' 'List of Tables' 'TOC \h \z \t "Table Caption,1"'

  # Gantt chart: its own landscape page (LaTeX uses pdflscape).
  foreach ($p in $doc.Paragraphs) {
    if ($p.Style.NameLocal -eq 'Image Caption' -and $p.Range.Text -like '*Gantt chart of SDP*') {
      $img = $p.Previous()
      $after = $doc.Range($p.Range.End, $p.Range.End); $after.InsertBreak(2)
      $before = $doc.Range($img.Range.Start, $img.Range.Start); $before.InsertBreak(2)
      $sec = $doc.Range($before.End, $before.End + 1).Sections.Item(1)
      $sec.PageSetup.Orientation = 1
      $shape = $sec.Range.InlineShapes.Item(1)
      $shape.LockAspectRatio = -1
      $shape.Width = 247*$mm
      $sec.Range.Paragraphs.Item(1).SpaceBefore = 0
      break
    }
  }

  # Page numbers, then refresh every field so the lists show page numbers.
  $ftr = $doc.Sections.Item(1).Footers.Item(1)
  $null = $ftr.PageNumbers.Add(1, $true)

  $doc.Fields.Update() | Out-Null
  foreach ($toc in $doc.TablesOfContents) { $toc.Update() }

  $doc.SaveAs2($Out, 16)
  if ($Pdf) { $doc.SaveAs2($Pdf, 17) }
  "pages: " + $doc.ComputeStatistics(2)
  "words: " + $doc.ComputeStatistics(0)
  "tables: " + $doc.Tables.Count
  "images: " + $doc.InlineShapes.Count
  $doc.Close($false); $doc = $null
} finally {
  if ($doc) { try { $doc.Close($false) } catch {} }
  $word.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}

