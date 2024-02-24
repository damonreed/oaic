#
# chat.py - utility functions for openai sdk
#
from .client import get_client

client = get_client()


def chat_response(system_role, user_role):
    response = (
        client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": user_role},
            ],
        )
        .choices[0]
        .message.content
    )
    return response
