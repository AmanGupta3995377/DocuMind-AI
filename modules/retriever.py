import numpy as np


class Retriever:

    def __init__(self):
        pass

    def cosine_similarity(self, a, b):

        return np.dot(a, b) / (
            np.linalg.norm(a) *
            np.linalg.norm(b)
        )

    def retrieve(
        self,
        query_embedding,
        chunk_embeddings,
        chunks,
        top_k=3
    ):

        scores = []

        for i, embedding in enumerate(chunk_embeddings):

            similarity = self.cosine_similarity(
                query_embedding,
                embedding
            )

            scores.append(
                (similarity, chunks[i])
            )

        scores.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return scores[:top_k]