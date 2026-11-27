
from app.analyzer.syntax_checker import check_syntax
from app.analyzer.error_detector import detect_runtime_error


def test_valid_python_code():

    code = """
x = 10
y = 20
print(x + y)
"""

    result = check_syntax(code)

    assert result["success"] is True


def test_invalid_python_code():

    code = """
if True
    print("Hello")
"""

    result = check_syntax(code)

    assert result["success"] is False
    assert result["error"]["type"] == "SyntaxError"


def test_code_compilation():

    code = """
x = 10
print(x)
"""

    result = detect_runtime_error(code)

    assert result["success"] is True
