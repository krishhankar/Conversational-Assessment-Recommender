from app.retrieval.catalog_loader import CatalogLoader
from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import VectorStore

loader = CatalogLoader()
catalog = loader.load_catalog()
vector_db = VectorStore()

ids = []
documents = []
embeddings = []
metadata = []

for assessment in catalog:
    ids.append(assessment.entity_id)
    document = assessment.embedding_text()
    documents.append(document)

    embeddings.append(EmbeddingModel.encode(document).tolist())

    metadata.append(
        {
            "name": assessment.name,
            "url": assessment.link,
            "duration": assessment.duration
        }
    )

vector_db.add_documents(ids, embeddings, documents, metadata)
print("Vector database built successfully.")
    