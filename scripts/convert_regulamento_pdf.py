"""Build Docs/Regulamento-Interno-CISCSR.pdf from the V4 docx text."""
import os
import textwrap
import zipfile
import xml.etree.ElementTree as ET

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.join(os.path.dirname(__file__), "..")
DOCX = os.path.join(ROOT, "Docs", "Confederação S.C. do REAA (V4).docx")
PDF = os.path.join(ROOT, "Docs", "Regulamento-Interno-CISCSR.pdf")
FONT = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "arial.ttf")
W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract_paragraphs(path):
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
    paras = []
    for p in root.iter(W_NS + "p"):
        texts = [t.text for t in p.iter(W_NS + "t") if t.text]
        if texts:
            paras.append("".join(texts))
    return paras


def wrap_paragraph(text, width=92):
  lines = []
  for block in text.split("\n"):
    block = block.strip()
    if not block:
      lines.append("")
      continue
    lines.extend(textwrap.wrap(block, width=width) or [""])
  return lines


def main():
    pdfmetrics.registerFont(TTFont("SiteFont", FONT))
    paras = extract_paragraphs(DOCX)
    c = canvas.Canvas(PDF, pagesize=A4)
    width, height = A4
    x = 20 * mm
    y = height - 20 * mm
    line_h = 5.2 * mm
    font_size = 10

    for para in paras:
        is_heading = (
            para.isupper()
            or para.startswith("TÍTULO")
            or para.startswith("Artigo")
            or para.startswith("PREÂMBULO")
            or para.startswith("REGULAMENTO")
            or set(para) == {"_"}
        )
        size = 11 if is_heading else font_size
        c.setFont("SiteFont", size)
        lines = wrap_paragraph(para, width=88 if is_heading else 92)
        block_h = len(lines) * (line_h + (0.8 * mm if is_heading else 0))
        if y - block_h < 20 * mm:
            c.showPage()
            y = height - 20 * mm
            c.setFont("SiteFont", size)
        for line in lines:
            if y < 20 * mm:
                c.showPage()
                y = height - 20 * mm
                c.setFont("SiteFont", size)
            c.drawString(x, y, line)
            y -= line_h
        y -= 2.5 * mm

    c.save()
    print(f"Wrote {PDF} ({os.path.getsize(PDF)} bytes)")


if __name__ == "__main__":
    main()
