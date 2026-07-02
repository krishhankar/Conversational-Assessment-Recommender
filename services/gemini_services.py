import json
import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME

class GeminiService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, user_prompt, system_prompt):
        response = self.model.generate_content([user_prompt, system_prompt])
        return response.text


