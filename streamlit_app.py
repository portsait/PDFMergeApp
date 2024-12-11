import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
from PyPDF2 import PdfMerger

# Streamlit PDF Merger App
st.title("PDF Merger")

# Upload multiple PDF files
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    merger = PdfMerger()

    for uploaded_file in uploaded_files:import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

# Streamlit PDF Merger App
st.title("PDF Merger")

# Upload multiple PDF files
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    merger = PdfMerger()

    for uploaded_file in uploaded_files:
        merger.append(uploaded_file)

    # Save the merged PDF to a BytesIO buffer
    merged_pdf = BytesIO()
    merger.write(merged_pdf)
    merger.close()
    merged_pdf.seek(0)

    # Display a download button for the merged PDF
    st.download_button(
        label="Download Merged PDF",
        data=merged_pdf,
        file_name="merged_document.pdf",
        mime="application/pdf"
    )

    st.success("PDF files have been merged successfully!")

        merger.append(uploaded_file)

    # Save the merged PDF to a BytesIO buffer
    merged_pdf = BytesIO()
    merger.write(merged_pdf)
    merger.close()
    merged_pdf.seek(0)

    # Display a download button for the merged PDF
    st.download_button(
        label="Download Merged PDF",
        data=merged_pdf,
        file_name="merged_document.pdf",
        mime="application/pdf"
    )

    st.success("PDF files have been merged successfully!")
