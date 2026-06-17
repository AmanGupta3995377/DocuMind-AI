import faiss
import numpy as np
import pickle


class VectorStore:

    def __init__(self):

        self.index = None

    def create_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            np.array(
                embeddings,
                dtype=np.float32
            )
        )

        print(
            f"FAISS Index Created ({self.index.ntotal} vectors)"
        )

    def save_index(
        self,
        index_path="data/processed_documents/faiss_index.bin"
    ):

        faiss.write_index(
            self.index,
            index_path
        )

        print(
            "FAISS Index Saved"
        )

    def load_index(
        self,
        index_path="data/processed_documents/faiss_index.bin"
    ):

        self.index = faiss.read_index(
            index_path
        )

        print(
            "FAISS Index Loaded"
        )

    def save_chunks(
        self,
        chunks,
        path="data/processed_documents/chunks.pkl"
    ):

        with open(
            path,
            "wb"
        ) as file:

            pickle.dump(
                chunks,
                file
            )

        print(
            "Chunks Saved"
        )

    def load_chunks(
        self,
        path="data/processed_documents/chunks.pkl"
    ):

        with open(
            path,
            "rb"
        ) as file:

            return pickle.load(
                file
            )