import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))


import streamlit as st
from modules.input_module import load_image, extract_text_from_pdf, extract_text_from_docx
from modules.ocr_module import image_to_text
import io

# Streamlit app config
st.set_page_config(page_title="OCR Extractor", layout="centered")
st.title("📄 OCR Text Extractor")
st.markdown("Upload an **image (JPG/PNG)**, **PDF**, or **Word file (.docx)** to extract text.")

# File uploader
uploaded_file = st.file_uploader("Upload File", type=["png", "jpg", "jpeg", "pdf", "docx"])

text = ""

if uploaded_file:
    file_type = uploaded_file.type

    if "image" in file_type:
        image = load_image(uploaded_file)
        if image:
            st.image(image, caption="Uploaded Image", use_column_width=True)
            if st.button("Extract Text"):
                with st.spinner("Extracting from image..."):
                    text = image_to_text(image)

    elif "pdf" in file_type:
        if st.button("Extract Text"):
            with st.spinner("Extracting from PDF..."):
                text = extract_text_from_pdf(uploaded_file)

    elif "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in file_type:
        if st.button("Extract Text"):
            with st.spinner("Extracting from Word..."):
                text = extract_text_from_docx(uploaded_file)

    if text:
        st.subheader("📜 Extracted Text:")
        st.text_area("Text Output", value=text, height=300)

        # Download as .txt
        output_bytes = io.BytesIO(text.encode("utf-8"))
        st.download_button(
            label="📥 Download Text File",
            data=output_bytes,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
    elif uploaded_file and not text:
        st.warning("No text extracted. Try another file.")
