from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="assessment recommender", version="1.0")
app.include_router(routes.router)

@app.get("/")
def home():
    return {"message": "welcome to the SHL Assessment Recommender"}

@app.get("/health")
def health():
    return {"status": "ok"}

    

