import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8,txt= f"Invoice nr. {filename.split('-')[0]}", align="L", ln=1, border=0)
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {filename.split('-')[1]}", align="L", ln=1, border=0)

    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    # Add a header
    columns = [items.replace('_', ' ').title() for items in df.columns]
    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt= columns[0], border=1)
    pdf.cell(w=60, h=8, txt= columns[1], border=1)
    pdf.cell(w=35, h=8, txt= columns[2], border=1)
    pdf.cell(w=30, h=8, txt= columns[3], border=1)
    pdf.cell(w=30, h=8, txt= columns[4], border=1, ln=1)

    # Add a rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.set_font(family="Times", style="B", size=13)
    pdf.cell(w=155, h=8, txt=" Total", border=1)
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence
    pdf.set_font(family="Times", size=10,style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
    # Add company name and logo
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"Danish Chaudhary ")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
