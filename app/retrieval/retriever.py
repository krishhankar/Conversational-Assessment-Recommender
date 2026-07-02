from config import TOP_K
from app.retrieval.vector_store import VectorStore 
from app.retrieval.embeddings import EmbeddingModel

class Retriever:

    def __init__(self):
        self.vector_db = VectorStore()

    def retrieve(self, query, top_k=TOP_K):

        embedding = EmbeddingModel.encode(query)

        results = self.vector_db.search(embedding.tolist(), top_k)

        recommendations = []

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0]

        for doc, meta, distance in zip(docs, metas, distances):
            recommendations.append(
                {
                    "name": meta["name"],
                    "url": meta["url"],
                    "duration": meta["duration"],
                    "document": doc,
                    "distance": distance
                }
            )

        return recommendations