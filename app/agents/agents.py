from app.agents.prompts import (ANALYZER_PROMPT, RECOMMENDATION_PROMPT)
from app.agents.parser import (parse_json)
from services.gemini_services import (GeminiService)
from app.retrieval.retriever import (Retriever)


class RecommendationAgent:

    def __init__(self):
        self.llm = GeminiService()
        self.retriever = Retriever()

    def run(self, query):
        analysis = self.llm.generate(ANALYZER_PROMPT, query)

        analysis = parse_json(analysis)

        action = analysis["action"]

        if action == "off_topic":

            return {
                "reply":
                "I'm designed only for SHL assessment recommendations."
            }

        if action == "clarification":

            return {
                "reply":
                "Could you provide: "
                + ", ".join(
                    analysis["missing_information"]
                )
            }

        if action == "recommendation":

            docs = self.retriever.retrieve(
                query
            )

            context = ""

            for item in docs:
                context += item["document"]
                context += "\n\n"
            final_prompt = f"""
User Query

{query}

Catalog Context

{context}

"""

            answer = self.llm.generate(RECOMMENDATION_PROMPT, final_prompt)

            return {
                "reply": answer,
                "recommendations": docs
            }

        if action == "comparison":

            return {
                "reply":
                "Comparison will be implemented next."
            }

        if action == "refinement":

            return {
                "reply":
                "Refinement will be implemented next."
            }