from modules.embeddings import EmbeddingGenerator
from modules.pdf_loader import PDFLoader
from modules.chunking import TextChunker


def main():

    print("=" * 50)
    print("DocuMind AI - PDF Extraction, Chunking & Embeddings Test")
    print("=" * 50)

    # Initialize PDF Loader
    loader = PDFLoader()

    # Load PDF
    text = loader.load_pdf("data/raw_documents/sample.pdf")

    # Display statistics
    print("\nPDF Statistics")
    print("-" * 50)
    print("Total Characters:", len(text))
    print("Total Words:", len(text.split()))

    # Save extracted text
    output_path = "data/processed_documents/extracted_text.txt"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"\nExtracted text saved to: {output_path}")

    # Initialize Chunker
    chunker = TextChunker(
        chunk_size=500,
        overlap=100
    )

    # Create Chunks
    chunks = chunker.create_chunks(text)

    print("\nChunking Statistics")
    print("-" * 50)
    print("Total Chunks Created:", len(chunks))
    print("Chunk Size:", chunker.chunk_size)
    print("Overlap:", chunker.overlap)

    # Generate Embeddings
    print("\nGenerating Embeddings...")

    embedding_generator = EmbeddingGenerator()

    embeddings = embedding_generator.generate_embeddings(
        chunks
    )

    print("\nEmbedding Statistics")
    print("-" * 50)
    print("Embedding Shape:", embeddings.shape)

    # Display first chunk
    print("\n" + "=" * 50)
    print("FIRST CHUNK")
    print("=" * 50)
    print(chunks[0])

    # Display second chunk
    if len(chunks) > 1:
        print("\n" + "=" * 50)
        print("SECOND CHUNK")
        print("=" * 50)
        print(chunks[1])

    # Display last chunk
    print("\n" + "=" * 50)
    print("LAST CHUNK")
    print("=" * 50)
    print(chunks[-1])

    # Save chunks to file
    chunks_output = "data/processed_documents/chunks.txt"

    with open(chunks_output, "w", encoding="utf-8") as file:

        for i, chunk in enumerate(chunks):
            file.write(f"\n\n{'='*50}\n")
            file.write(f"CHUNK {i+1}\n")
            file.write(f"{'='*50}\n")
            file.write(chunk)

    print(f"\nChunks saved to: {chunks_output}")

    print("\nDocuMind AI Pipeline Completed Successfully!")


if __name__ == "__main__":
    main()