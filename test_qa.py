from modules.embeddings import EmbeddingGenerator
from modules.qa_system import QASystem


embedding_generator = EmbeddingGenerator()

qa_system = QASystem()

question = input(
    "\nEnter your question: "
)

answer = qa_system.answer_question(
    question,
    embedding_generator
)

print("\nANSWER")
print("=" * 50)
print(answer)