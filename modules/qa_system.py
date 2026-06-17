from modules.retriever import Retriever
from llm.gemini_adapter import GeminiAdapter


class QASystem:

    def __init__(self):

        self.retriever = Retriever()
        self.llm = GeminiAdapter()

    def answer_question(
        self,
        question,
        chunk_embeddings,
        chunks,
        embedding_generator
    ):

        query_embedding = (
            embedding_generator.model.encode(
                question
            )
        )

        results = self.retriever.retrieve(
            query_embedding,
            chunk_embeddings,
            chunks,
            top_k=3
        )

        context = ""

        for score, chunk in results:
            context += chunk + "\n\n"

        prompt = f"""
You are a document question answering assistant.

Answer the question ONLY using the provided context.

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