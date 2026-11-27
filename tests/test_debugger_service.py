
from app.services.debugger import debug_code


sample_code = """
age = 25
message = "Your age is " + age
print(message)
"""

result = debug_code(sample_code)

print("\nSYNTAX CHECK:")
print(result["syntax_check"])

print("\nAI DEBUGGING RESULT:")
print("=" * 50)
print(result["ai_analysis"])
