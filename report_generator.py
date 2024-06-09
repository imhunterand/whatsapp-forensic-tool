from fpdf import FPDF

def generate_report(messages):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for message in messages:
        pdf.cell(200, 10, txt=str(message), ln=True)

    pdf.output("forensic_report.pdf")