
from openai import OpenAI, APIStatusError
from app.utils.config import NVIDIA_API_KEY, NVIDIA_BASE_URL

client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url=NVIDIA_BASE_URL,
    timeout=30.0
)

print("Checking NVIDIA API access...")

try:
    models = client.models.list()

    print("\nAvailable model IDs:")
    print("=" * 50)

    for model in models.data:
        print(model.id)

except APIStatusError as error:
    print("\nNVIDIA API ERROR")
    print("Status:", error.status_code)
    print("Response:", error.response.text)

except Exception as error:
    print(type(error).__name__, str(error))
