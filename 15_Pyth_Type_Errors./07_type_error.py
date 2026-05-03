# This is raised when an operation or function is applied to an object of an inappropriate data type. For example, adding a string to an integer.
# ❌ Incorrect: Cannot add string and integer directly
# result = "The answer is " + 42

# ✅ Correct: Convert integer to string first
result = "The answer is " + str(42)
print(result)  # Output: The answer is 42
