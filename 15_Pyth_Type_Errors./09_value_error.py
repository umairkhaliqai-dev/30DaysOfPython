# This error is raised when a function receives an argument that has the correct type but an inappropriate value. A classic example is trying to convert a non-numeric string into an integer.
# ❌ Incorrect: The string 'hello' cannot be converted to an integer
# number = int("hello")

# ✅ Correct: Provide a numeric string
number = int("123")
print(number)  # Output: 123