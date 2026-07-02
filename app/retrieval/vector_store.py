import chromadb
from config import CHROMA_DB, TOP_K

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_DB)
        self.collection = self.client.get_or_create_collection(name="shl_catalog")

    def add_documents(self, ids, embeddings, documents, metadatas):
        self.collection.upsert(
            ids = ids,
            embeddings = embeddings,
            documents = documents,
            metadatas = metadatas
        )

    def search(self,embedding,top_k=TOP_K):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )