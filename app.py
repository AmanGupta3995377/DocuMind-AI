from modules.pdf_loader import PDFLoader


def main():

    print("=" * 50)
    print("DocuMind AI - PDF Extraction Test")
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

    # Show beginning of PDF
    print("\n" + "=" * 50)
    print("FIRST 1000 CHARACTERS")
    print("=" * 50)
    print(text[:1000])

    # Show ending of PDF
    print("\n" + "=" * 50)
    print("LAST 1000 CHARACTERS")
    print("=" * 50)
    print(text[-1000:])

    print("\nPDF Extraction Completed Successfully!")


if __name__ == "__main__":
    main()