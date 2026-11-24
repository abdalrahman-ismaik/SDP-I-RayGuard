-- Pandoc filter for build-docx.ps1: put the citeproc bibliography where
-- docx_prep.py left REFS-PLACEHOLDER (after Chapter 6, before the appendices).
function Para(el)
  if pandoc.utils.stringify(el) == "REFS-PLACEHOLDER" then
    return pandoc.Div({}, pandoc.Attr("refs"))
  end
end
