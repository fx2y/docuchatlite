class DocumentChunker:
    def __init__(self, window_size, stride):
        self.window_size = window_size
        self.stride = stride

    def generate_chunks(self, document):
        chunks = []
        start = 0
        while start + self.window_size <= len(document):
            chunk = document[start:start + self.window_size]
            chunks.append(chunk)
            start += self.stride
        return chunks
