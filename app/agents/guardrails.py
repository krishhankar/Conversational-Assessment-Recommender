BLOCKED_WORDS = [
    "ignore previous instructions",
    "forget your instructions",
    "system prompt",
    "jailbreak"
]

def is_prompt_injection(query):
    query = query.lower()

    return any(word in query for word in BLOCKED_WORDS)