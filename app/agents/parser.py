import json


def parse_json(text):

    try:
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
        return json.loads(text)

    except Exception:

        return {

            "action": "clarification",

            "enough_information": False,

            "missing_information": [
                "Unable to parse response"
            ]

        }