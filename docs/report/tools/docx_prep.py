"""Flatten the report LaTeX into a form Pandoc reads well.

Usage: python docx_prep.py <report_dir> <out.tex>

Called by build-docx.ps1. Run the LaTeX build first: heading, table, figure
and equation numbers are copied from build/main.aux and build/main.toc so the
Word copy matches the PDF. The custom column types (L, Y), \\tablesetup and
longtables are rewritten as plain tabular environments with explicit widths.
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
out = Path(sys.argv[2])
BS = chr(92)


def braced(s, i):
    """Return (content, end_index) of the {...} group starting at s[i]."""
    assert s[i] == "{", s[i:i + 40]
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    raise ValueError("unbalanced")


def inline_inputs(text):
    def rep(m):
        p = root / (m.group(1) + ".tex")
        return p.read_text(encoding="utf-8")
    return re.sub(r"\\input\{([^}]*)\}", rep, text)


src = inline_inputs((root / "main.tex").read_text(encoding="utf-8"))
aux = (root / "build" / "main.aux").read_text(encoding="utf-8")
toc = (root / "build" / "main.toc").read_text(encoding="utf-8")

labels = {}
for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", aux):
    labels[m.group(1)] = m.group(2)

toc_numbers = re.findall(r"\\contentsline \{(?:chapter|section|subsection)\}\{\\numberline \{([^}]*)\}", toc)

# Strip comments (unescaped %).
src = "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in src.split("\n"))

body = src[src.index(BS + "begin{document}") + len(BS + "begin{document}"):src.index(BS + "end{document}")]

# Title page -> plain centred block (centred later in Word).
tp_start = body.index(BS + "begin{titlepage}")
tp_end = body.index(BS + "end{titlepage}") + len(BS + "end{titlepage}")
title = r"""
TITLEPAGE-START

Khalifa University of Science and Technology

College of Computing and Mathematical Sciences

Department of Computer Science

TITLE-RAYGUARD

AI-Powered Explosive Detection in X-ray Scans

Senior Design Project I

Final Report

Team Members

Abd Alrahman Ismaik --- Computer Science

Faisal Daoud Alzarooni --- Computer Science

Ali Arif Saeed Alshamsi --- Computer Science

Mohammad Arwani --- Computer Science

Ahmed Almansoori --- Computer Science

Supervisor

Prof. Naoufel Werghi

Fall 2026 --- November 2026

TITLEPAGE-END
"""
# Keep this block in step with the titlepage in main.tex.
tp_src = body[tp_start:tp_end]
tp_plain = re.sub(r"\\[a-zA-Z]+|\[[^\]]*\]|[{}\\]", " ", tp_src)
tp_plain = " ".join(tp_plain.split())
for line in title.strip().splitlines():
    text = line.split(" --- ")[0].strip()
    if not text or text.isupper():  # blank lines and markers
        continue
    if text not in tp_plain:
        sys.exit(f"Title page text not found in main.tex: {text!r}; update docx_prep.py")
body = body[:tp_start] + title + body[tp_end:]

# Front-matter commands Pandoc cannot render; TOC/LoF/LoT are inserted in Word.
for cmd in ["hypersetup", "pagenumbering", "addcontentsline", "bibliographystyle"]:
    body = re.sub(BS * 2 + cmd + r"(\{[^{}]*\})+", "", body)
body = body.replace(BS + "tableofcontents", "\nTOC-PLACEHOLDER\n")
body = body.replace(BS + "listoffigures", "\nLOF-PLACEHOLDER\n")
body = body.replace(BS + "listoftables", "\nLOT-PLACEHOLDER\n")
body = body.replace(BS + "clearpage", "")
body = re.sub(r"\\bibliography\{[^}]*\}", lambda m: "\n" + BS + "chapter*{References}\n\nREFS-PLACEHOLDER\n", body)
body = body.replace(BS + "appendix", "")
body = body.replace(BS + "makeatletter", "").replace(BS + "makeatother", "")

# \IfFileExists{path}{yes}{no}: keep the branch LaTeX would take.
def resolve_if_exists(text):
    key = BS + "IfFileExists{"
    while key in text:
        i = text.index(key)
        path, j = braced(text, i + len(key) - 1)
        yes, k = braced(text, j)
        no, end = braced(text, k)
        text = text[:i] + (yes if (root / path).exists() else no) + text[end:]
    return text


body = resolve_if_exists(body)

# Macros.
body = re.sub(r"\\begingroup\\tablesetup|\\endgroup|\\tablesetup", "", body)
body = re.sub(r"\\projectrecord\{([^}]*)\}", r"\\textit{Project evidence:} \\texttt{\1}.", body)
body = re.sub(r"\\file\{([^}]*)\}", r"\\texttt{\1}", body)
body = body.replace(BS + "pending{", BS + "textbf{Pending verification:} {")
body = re.sub(r"\\cite[pt]\{", lambda m: BS + "cite{", body)
body = body.replace(BS + "centering", "")

# Headings: attach numbers from the TOC, in order.
it = iter(toc_numbers)


def head(m):
    return f"{BS}{m.group(1)}*{{{next(it)}\u2003"


body = re.sub(r"\\(chapter|section|subsection)\{", head, body)
body = body.replace(BS + "chapter*{", BS + "chapter*{")

# References to labels.
body = re.sub(r"\\(?:eq)?ref\{([^}]*)\}", lambda m: labels.get(m.group(1), "??"), body)


def colspec(spec):
    spec = spec.replace("@{}", "")
    cols = []
    i = 0
    while i < len(spec):
        c = spec[i]
        if c in "LpP":
            w, i = braced(spec, i + 1)
            cols.append(("p", float(re.match(r"[\d.]+", w).group(0))))
            continue
        if c in "lcrY X":
            if c.strip():
                cols.append((c, None))
        i += 1
    fixed = sum(w for k, w in cols if k == "p") + 0.07 * sum(1 for k, _ in cols if k in "lcr")
    flex = [k for k, _ in cols if k in "YX"]
    yw = max(0.12, (0.97 - fixed) / len(flex)) if flex else 0
    parts = []
    for k, w in cols:
        if k == "p":
            parts.append(f"p{{{w:.3f}{BS}textwidth}}")
        elif k in "YX":
            parts.append(f"p{{{yw:.3f}{BS}textwidth}}")
        else:
            parts.append(f"p{{0.07{BS}textwidth}}")
    return "".join(parts)


def caption_prefix(env_text, kind):
    m = re.search(r"\\label\{([^}]*)\}", env_text)
    if not m:
        return env_text
    num = labels.get(m.group(1), "?")
    word = "Table" if kind == "table" else "Figure"
    return env_text.replace(BS + "caption{", f"{BS}caption{{{word} {num}: ", 1)


# tabularx -> tabular with explicit widths.
def fix_tabularx(text):
    key = BS + "begin{tabularx}"
    while key in text:
        i = text.index(key)
        _, j = braced(text, i + len(key))
        spec, k = braced(text, j)
        text = text[:i] + BS + "begin{tabular}{" + colspec(spec) + "}" + text[k:]
    return text.replace(BS + "end{tabularx}", BS + "end{tabular}")


def fix_tabular(text):
    key = BS + "begin{tabular}{"
    pos = 0
    while True:
        i = text.find(key, pos)
        if i < 0:
            return text
        spec, k = braced(text, i + len(key) - 1)
        new = colspec(spec) if ("@" in spec or "L" in spec or "Y" in spec) else spec
        text = text[:i] + key + new + "}" + text[k:]
        pos = i + 1


def fix_longtable(text):
    key = BS + "begin{longtable}"
    while key in text:
        i = text.index(key)
        spec, j = braced(text, i + len(key))
        end = text.index(BS + "end{longtable}", j)
        inner = text[j:end]
        cap = ""
        m = re.search(r"\\caption\{", inner)
        if m:
            c, ce = braced(inner, m.end() - 1)
            rest = inner[ce:]
            lab = re.match(r"\s*\\label\{[^}]*\}", rest)
            lab_s = lab.group(0) if lab else ""
            rest = rest[len(lab_s):]
            rest = re.sub(r"^\s*\\\\", "", rest)
            cap = f"{BS}caption{{{c}}}{lab_s.strip()}\n"
            inner = inner[:m.start()] + rest
        # Drop repeated header (\endhead block) and the endfirsthead marker.
        if BS + "endhead" in inner:
            a = inner.index(BS + "endfirsthead")
            b = inner.index(BS + "endhead")
            inner = inner[:a] + inner[b + len(BS + "endhead"):]
        inner = re.sub(r"\\end(firsthead|foot|lastfoot)", "", inner)
        block = (f"{BS}begin{{table}}\n{cap}{BS}begin{{tabular}}{{{colspec(spec)}}}"
                 f"{inner}{BS}end{{tabular}}\n{BS}end{{table}}")
        text = text[:i] + block + text[end + len(BS + "end{longtable}"):]
    return text


body = fix_longtable(fix_tabular(fix_tabularx(body)))

# Caption numbers.
def number_floats(text, env):
    out_parts = []
    pos = 0
    pat = re.compile(r"\\begin\{" + env + r"\}(\[[^\]]*\])?")
    for m in pat.finditer(text):
        if m.start() < pos:
            continue
        end = text.index(BS + "end{" + env + "}", m.end())
        out_parts.append(text[pos:m.start()])
        out_parts.append(caption_prefix(text[m.start():end], env))
        pos = end
    out_parts.append(text[pos:])
    return "".join(out_parts)


body = number_floats(body, "table")
body = number_floats(body, "figure")

# Equation numbers: number per chapter, in order.
chap = None
eq_count = 0
parts = []
pos = 0
for m in re.finditer(r"\\chapter\*\{([0-9A-Z]+)\u2003|\\begin\{equation\}", body):
    if m.group(0).startswith(BS + "chapter"):
        chap, eq_count = m.group(1), 0
        continue
    eq_count += 1
    end = body.index(BS + "end{equation}", m.end())
    parts.append(body[pos:m.start()])
    eq = re.sub(r"\\label\{[^}]*\}", "", body[m.end():end])
    parts.append(f"{BS}begin{{equation}}{eq}\\qquad\\qquad({chap}.{eq_count}){BS}end{{equation}}")
    pos = end + len(BS + "end{equation}")
parts.append(body[pos:])
body = "".join(parts)

preamble = BS + "documentclass{report}\n" + BS + "begin{document}\n"
out.write_text(preamble + body + "\n" + BS + "end{document}\n", encoding="utf-8")
print("labels", len(labels), "toc numbers", len(toc_numbers), "unused", len(list(it)))
