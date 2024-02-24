import sys
from . import gcp_secret as secret
from openai import OpenAI

api_key = secret.get("OPENAI_API_KEY")


# return an authenticated OpenAI client
def get_client() -> OpenAI:
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print("Failed to create OpenAI client:", e)
        sys.exit(1)
    return client
