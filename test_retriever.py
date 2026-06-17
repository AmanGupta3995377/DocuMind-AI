from modules.embeddings import EmbeddingGenerator
from modules.pdf_loader import PDFLoader
from modules.chunking import TextChunker
from modules.retriever import Retriever

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

query = "What is cybersecurity management?"

query_embedding = (
    embedding_generator.model.encode(
        query
    )
)

retriever = Retriever()

results = retriever.retrieve(
    query_embedding,
    chunk_embeddings,
    chunks,
    top_k=3
)

print("\nTOP RESULTS")
print("=" * 50)

for rank, (score, chunk) in enumerate(results, start=1):

    print(f"\nResult {rank}")
    print(f"Similarity: {score:.4f}")
    print("-" * 50)

    print(chunk[:500])