# This occurs when you try to access a sequence (like a list, tuple, or string) using an index that is outside its valid range (e.g., index is too high or negative beyond the start).
fruits = ["apple", "banana", "cherry"]
# ❌ Incorrect: Index 3 does not exist (max index is 2)
# print(fruits[3])

# ✅ Correct:
print(fruits[2])  # Output: cherry