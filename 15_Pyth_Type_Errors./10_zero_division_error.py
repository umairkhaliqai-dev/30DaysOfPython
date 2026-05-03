# This specific arithmetic error is raised when you try to divide a number by zero in any mathematical operation (division or modulo).

# ❌ Incorrect: Division by zero is mathematically undefined
# result = 10 / 0

# ✅ Correct: Ensure denominator is not zero
denominator = 2
if denominator != 0:
    result = 10 / denominator
    print(result)  # Output: 5.0

  