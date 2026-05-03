# A concise, Pythonic way to create new lists from existing iterables — all in a single line.
# Get only even numbers from 0–19
evens = [n for n in range(20) if n % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print()
# Make all words UPPERCASE from a sentence
words = ["python", "is", "fun"]
upper = [w.upper() for w in words]
print(upper)
# ['PYTHON', 'IS', 'FUN']
print()
# Flatten: numbers greater than 5, squared
result = [n**2 for n in range(10) if n > 5]
print(result)
# [36, 49, 64, 81]