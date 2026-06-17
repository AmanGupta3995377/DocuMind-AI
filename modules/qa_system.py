from modules.vector_store import VectorStore
from llm.gemini_adapter import GeminiAdapter


class QASystem:

    def __init__(self):

        self.vector_store = VectorStore()

        self.vector_store.load_index()

        self.chunks = self.vector_store.load_chunks()

        self.llm = GeminiAdapter()

    def answer_question(
        self,
        question,
        embedding_generator
    ):

        query_embedding = (
            embedding_generator.model.encode(
                question
            )
        )

        indices = self.vector_store.search(
            query_embedding,
            top_k=3
        )

        context = ""

        for idx in indices:

            context += (
                self.chunks[idx]
                + "\n\n"
            )

        prompt = f"""
You are a document question answering assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = self.llm.generate_response(
            prompt
        )

        return answer