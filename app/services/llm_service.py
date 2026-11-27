
from openai import OpenAI

from app.utils.config import (
    NVIDIA_API_KEY,
    NVIDIA_BASE_URL,
    NVIDIA_MODEL,
    validate_config
)


def get_ai_client():

    validate_config()

    return OpenAI(
        api_key=NVIDIA_API_KEY,
        base_url=NVIDIA_BASE_URL,
        timeout=90.0,
        max_retries=1
    )


def ask_ai(prompt: str):

    client = get_ai_client()

    response = client.chat.completions.create(
        model=NVIDIA_MODEL,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert Python debugging assistant. "
                    "Find programming errors, explain their causes "
                    "and provide corrected code."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=1.0,
        top_p=0.95,
        max_tokens=1024,
        stream=False
    )

    return response.choices[0].message.content
