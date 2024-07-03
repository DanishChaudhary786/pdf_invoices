import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P",unit="mm",format="A4")
for filepath in filepaths:
    print(filepath)
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=filename.title(), align="L", ln=1, border=0)
    with open(filepath) as file:
        lines = file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=190, h=10, txt=lines)

pdf.output("files/output.pdf")