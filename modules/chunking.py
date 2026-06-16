class TextChunker:

    def __init__(self, chunk_size=500, overlap=100):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def create_chunks(self, text):

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks