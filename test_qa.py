from modules.pdf_loader import PDFLoader
from modules.chunking import TextChunker
from modules.embeddings import EmbeddingGenerator
from modules.qa_system import QASystem


loader = PDFLoader()

text = loader.load_pdf(
    "data/raw_documents/sample.pdf"
)

chunker = TextChunker(
    chunk_size=500,
    overlap=100
)

chunks = chunker.create_chunks(text)

embedding_generator = EmbeddingGenerator()

chunk_embeddings = (
    embedding_generator.generate_embeddings(
        chunks
    )
)

qa_system = QASystem()

question = input(
    "\nEnter your question: "
)

answer = qa_system.answer_question(
    question,
    chunk_embeddings,
    chunks,
    embedding_generator
)

print("\nANSWER")
print("=" * 50)
print(answer)