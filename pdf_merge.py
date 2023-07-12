import os
from PyPDF2 import PdfMerger
import streamlit as st

def merge_pdfs(directory, output_path):
    merger = PdfMerger()

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            merger.append(filepath)

    merger.write(output_path)
    merger.close()

    return output_path

def main():
    st.title("PDF Merge")

    # File directory selection
    directory = st.sidebar.selectbox(
        "Select the directory path where PDFs are located:",
        os.listdir("."),
    )

    # Output filename
    output_filename = st.sidebar.text_input("Enter the output filename for the merged PDF:", "merged_output")

    # Merge PDFs
    if st.button("Merge PDFs"):
        with st.spinner("Merging PDFs..."):
            #with st.beta_expander("Show Progress"):
            output_path = os.path.join(directory, f"{output_filename}.pdf")
            merge_pdfs(directory, output_path)
            st.success(f"PDFs merged into {output_filename}.pdf successfully!")

        # Provide download link
        abs_ouput_path = os.path.abspath(output_path)
        st.markdown(f"Download the merged PDF: [Download {output_filename}.pdf]({abs_ouput_path})", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

