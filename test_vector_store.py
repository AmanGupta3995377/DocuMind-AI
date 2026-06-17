from modules.pdf_loader import PDFLoader
from modules.chunking import TextChunker
from modules.embeddings import EmbeddingGenerator
from modules.vector_store import VectorStore


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

embeddings = (
    embedding_generator.generate_embeddings(
        chunks
    )
)

vector_store = VectorStore()

vector_store.create_index(
    embeddings
)

vector_store.save_index()

vector_store.save_chunks(
    chunks
)

print("\nVector Store Ready")