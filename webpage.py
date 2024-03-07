import streamlit as st
from askLLama import askllama
import os

def webpage():
    st.title("PDF ChatBot")
    # File upload widget
    pdf = st.file_uploader('Choose your .pdf file', type="pdf")

    if pdf is not None:
        # Create 'temp' directory if it doesn't exist
        temp_dir = "/Users/daanishhindustano/Documents/projects/Bookify/BookifyPDF's"

        # Save the uploaded file to a temporary location
        pdf_path = os.path.join(temp_dir, pdf.name)
        with open(pdf_path, "wb") as f:
            f.write(pdf.read())

        question = st.text_input("Enter your question:")
        
        if st.button("Ask Llama", key="ask_button"):
            with st.spinner("Asking Llama..."):
                response = askllama(pdf_path, question)
                st.success("Done!")
                st.write(response)
 

