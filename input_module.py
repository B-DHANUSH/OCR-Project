from PIL import Image
import pdfplumber
from docx import Document

def load_image(uploaded_file):
    try:
        return Image.open(uploaded_file)
    except:
        return None

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def extract_text_from_docx(uploaded_file):
    doc = Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])
