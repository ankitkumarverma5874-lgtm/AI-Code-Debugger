
import ast


def check_syntax(code: str):

    try:
        # Parse the Python source code
        ast.parse(code)

        return {
            "success": True,
            "error": None,
            "message": "No syntax errors found."
        }

    except SyntaxError as error:

        return {
            "success": False,
            "error": {
                "type": "SyntaxError",
                "message": error.msg,
                "line": error.lineno,
                "column": error.offset
            },
            "message": "Syntax error detected."
        }
