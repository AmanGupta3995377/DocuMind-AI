import os
import streamlit as st

from modules.document_processor import DocumentProcessor
from modules.embeddings import EmbeddingGenerator
from modules.qa_system import QASystem


st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 DocuMind AI")

st.write(
    "Upload a PDF and ask questions."
)

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = os.path.join(
        "data/raw_documents",
        uploaded_file.name
    )

    with open(
        save_path,
        "wb"
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )

    if st.button(
        "Process PDF"
    ):

        processor = (
            DocumentProcessor()
        )

        with st.spinner(
            "Processing PDF..."
        ):

            processor.process_document(
                save_path
            )

        st.cache_resource.clear()

        st.success(
            "PDF Processed Successfully!"
        )


@st.cache_resource
def load_system():

    embedding_generator = (
        EmbeddingGenerator()
    )

    qa_system = (
        QASystem()
    )

    return (
        embedding_generator,
        qa_system
    )


embedding_generator, qa_system = (
    load_system()
)

question = st.text_input(
    "Ask a Question"
)

if st.button(
    "Get Answer"
):

    if question:

        with st.spinner(
            "Searching..."
        ):

            answer = (
                qa_system.answer_question(
                    question,
                    embedding_generator
                )
            )

        st.subheader(
            "Answer"
        )

        st.write(
            answer
        )