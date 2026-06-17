from modules.embeddings import EmbeddingGenerator
from modules.vector_store import VectorStore

embedding_generator = EmbeddingGenerator()

vector_store = VectorStore()

vector_store.load_index()

chunks = vector_store.load_chunks()

question = input(
    "\nEnter Question: "
)

query_embedding = (
    embedding_generator.model.encode(
        question
    )
)

indices = vector_store.search(
    query_embedding,
    top_k=3
)

print("\nTOP MATCHES")
print("=" * 50)

for idx in indices:

    print("\n")
    print(chunks[idx][:500])
    print("-" * 50)