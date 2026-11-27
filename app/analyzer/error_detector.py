
import traceback


def detect_runtime_error(code: str):

    try:
        # Compile source without executing it
        compiled_code = compile(
            code,
            "<user_code>",
            "exec"
        )

        return {
            "success": True,
            "error": None,
            "message": "Code compiled successfully."
        }

    except Exception as error:

        return {
            "success": False,
            "error": {
                "type": type(error).__name__,
                "message": str(error)
            },
            "message": "Compilation failed."
        }
