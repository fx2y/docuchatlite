from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ChunkSelector:
    def __init__(self, top_k):
        self.top_k = top_k
        self.vectorizer = TfidfVectorizer()

    def select_chunks(self, query, chunks):
        chunk_scores = []
        for chunk in chunks:
            similarity_score = self._calculate_similarity(query, chunk)
            chunk_scores.append(similarity_score)
        sorted_indices = sorted(range(len(chunk_scores)), key=lambda i: chunk_scores[i], reverse=True)
        top_k_indices = sorted_indices[:self.top_k]
        top_k_chunks = [chunks[i] for i in top_k_indices]
        return top_k_chunks

    def _calculate_similarity(self, query, chunk):
        corpus = [query, chunk]
        vectors = self.vectorizer.fit_transform(corpus)
        similarity_matrix = cosine_similarity(vectors)
        return similarity_matrix[0][1]
