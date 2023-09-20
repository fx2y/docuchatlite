from chunk_selector import ChunkSelector
from document_chunker import DocumentChunker

document_chunker = DocumentChunker(window_size=10, stride=5)
chunk_selector = ChunkSelector(top_k=2)

# To generate chunks from a document and select the top-k chunks for a query:
document = "This is an example document."
query = "example"
chunks = document_chunker.generate_chunks(document)
top_k_chunks = chunk_selector.select_chunks(query, chunks)
print(top_k_chunks)