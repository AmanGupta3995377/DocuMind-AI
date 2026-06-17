from modules.embeddings import EmbeddingGenerator
from modules.qa_system import QASystem


def main():

    print("=" * 60)
    print("DocuMind AI")
    print("=" * 60)

    embedding_generator = EmbeddingGenerator()

    qa_system = QASystem()

    while True:

        question = input(
            "\nAsk a Question (or type 'exit'): "
        )

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        answer = qa_system.answer_question(
            question,
            embedding_generator
        )

        print("\n" + "=" * 60)
        print("ANSWER")
        print("=" * 60)
        print(answer)


if __name__ == "__main__":
    main()