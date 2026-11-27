
import os
from dotenv import load_dotenv

# Load environment variables from project root
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

NVIDIA_BASE_URL = os.getenv(
    "NVIDIA_BASE_URL",
    "https://integrate.api.nvidia.com/v1"
)

NVIDIA_MODEL = os.getenv(
    "NVIDIA_MODEL",
    "qwen/qwen3-next-80b-a3b-instruct"
)


def validate_config():

    if not NVIDIA_API_KEY:
        raise ValueError(
            "NVIDIA_API_KEY is missing. Check your .env file."
        )

    return True
