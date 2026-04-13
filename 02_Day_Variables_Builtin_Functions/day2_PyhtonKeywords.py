# Exercise 14: Check Python reserved keywords
print("=== EXERCISE 14: Python Keywords ===\n")
print("To see all Python keywords, run this in your terminal:")
print("python3 -c \"import keyword; print(keyword.kwlist)\"")
print("\nOr in Python interactive shell, type: help('keywords')\n")

# Bonus: Show keywords in the output
import keyword
print("Python Reserved Keywords:")
print(keyword.kwlist)
