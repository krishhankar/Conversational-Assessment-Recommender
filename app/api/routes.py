from fastapi import APIRouter
from app.schema.request import RecommendationRequest
from app.agents.agents import RecommendationAgent

router = APIRouter()

agent = RecommendationAgent()

@router.post("/recommend")
def recommend(request: RecommendationRequest):
    response = agent.run(request.query)

    return response

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }