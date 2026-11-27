
from app.analyzer.syntax_checker import check_syntax
from app.services.llm_service import ask_ai


def debug_code(code: str):
    # Step 1: Check Python syntax
    syntax_result = check_syntax(code)

    # Step 2: Prepare prompt for AI
    if syntax_result["success"]:
        error_details = "No syntax error detected."
    else:
        error_details = str(syntax_result["error"])

    prompt = f"""
You are an expert Python debugging assistant.

Analyze the following Python code.

CODE:
{code}

DETECTED ERROR:
{error_details}

Provide your response in these sections:

1. Error detected
2. Reason for the error
3. Corrected Python code
4. Beginner-friendly explanation

If the code has no syntax error, inspect it for other
obvious programming mistakes. Do not claim that runtime
execution was performed.
"""

    # Step 3: Get AI analysis
    ai_response = ask_ai(prompt)

    # Step 4: Return complete result
    return {
        "syntax_check": syntax_result,
        "ai_analysis": ai_response
    }
