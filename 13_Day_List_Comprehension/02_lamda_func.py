# An anonymous, one-line function — perfect for small, throw-away operations where writing a full def would be overkill.
# Lambda with one argument
square = lambda x: x ** 2
print(square(6))
# 36
print()
# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(4, 7))
# 28
print()
# Lambda used with sorted() to sort by key
names = ["Charlie", "Alice", "Bob"]
sorted_names = sorted(names, key= lambda n: len(n))
print(sorted_names)
# ['Bob', 'Alice', 'Charlie']