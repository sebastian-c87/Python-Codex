import os
from typing import List

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


def get_refactor_suggestions(code: str) -> str:
    """Send code to OpenAI ChatCompletion API and return suggestions."""
    if not openai.api_key:
        return "OpenAI API key not set"

    prompt = (
        "You are an assistant that reviews Python code. Identify potential bugs, "
        "suggest improvements and refactorings. Provide short explanations."
    )
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"```python\n{code}\n```"},
    ]

    response = openai.ChatCompletion.create(model=MODEL_NAME, messages=messages)
    return response.choices[0].message.content.strip()
