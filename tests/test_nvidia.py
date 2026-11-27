
from app.services.llm_service import ask_ai


def main():

    prompt = """
    Explain this Python error:

    TypeError: unsupported operand type(s)
    for +: 'int' and 'str'

    Give:
    1. Reason for the error
    2. Corrected Python code
    3. Explanation for a beginner
    """

    print("Connecting to NVIDIA AI...")

    try:
        response = ask_ai(prompt)

        print("\nAI RESPONSE:")
        print("=" * 50)
        print(response)

    except Exception as error:
        print("AI connection failed:")
        print(type(error).__name__, str(error))


if __name__ == "__main__":
    main()
