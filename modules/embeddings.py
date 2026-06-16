from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding Model Loaded Successfully")

    def generate_embeddings(self, chunks):

        embeddings = self.model.encode(
            chunks,
            show_progress_bar=True
        )

        return embeddings