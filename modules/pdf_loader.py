import fitz


class PDFLoader:

    def __init__(self):
        print("PDF Loader Initialized")

    def load_pdf(self, pdf_path):

        document = fitz.open(pdf_path)

        extracted_text = ""

        for page in document:
            extracted_text += page.get_text()

        document.close()

        print(f"Total Characters Extracted: {len(extracted_text)}")

        return extracted_text