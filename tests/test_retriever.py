from app.retrieval.retriever import Retriever


retriever = Retriever()

results = retriever.retrieve("Hiring Java Backend Developer")

print(results)