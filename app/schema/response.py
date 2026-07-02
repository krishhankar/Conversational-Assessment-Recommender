from pydantic import BaseModel
from typing import List

class Assessment(BaseModel):
    name: str
    url: str
    duration: str

class RecommendationResponse(BaseModel):
    reply: str
    recommendations: List[Assessment]