from app.agents.agents import RecommendationAgent

agent = RecommendationAgent()

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break
    
    response = agent.run(query)
    print(response)