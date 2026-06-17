from modules.pdf_loader import PDFLoader
from modules.chunking import TextChunker
from modules.embeddings import EmbeddingGenerator
from modules.vector_store import VectorStore


class DocumentProcessor:

    def __init__(self):

        self.loader = PDFLoader()

        self.chunker = TextChunker(
            chunk_size=500,
            overlap=100
        )

        self.embedding_generator = (
            EmbeddingGenerator()
        )

        self.vector_store = (
            VectorStore()
        )

    def process_document(
        self,
        pdf_path
    ):

        print("Loading PDF...")

        text = self.loader.load_pdf(
            pdf_path
        )

        print("Creating Chunks...")

        chunks = self.chunker.create_chunks(
            text
        )

        print("Generating Embeddings...")

        embeddings = (
            self.embedding_generator.generate_embeddings(
                chunks
            )
        )

        print("Creating FAISS Index...")

        self.vector_store.create_index(
            embeddings
        )

        self.vector_store.save_index()

        self.vector_store.save_chunks(
            chunks
        )

        print(
            "Document Indexed Successfully"
        )