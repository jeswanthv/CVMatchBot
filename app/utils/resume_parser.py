import pdfplumber
from docx import Document


def parse_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])


def parse_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])
