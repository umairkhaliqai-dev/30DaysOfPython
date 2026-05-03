# filter(function, iterable) constructs an iterator from elements of the iterable for which the function returns True. The function should return a boolean.

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8]

# Filter words longer than 3 letters
words = ["cat", "elephant", "dog", "bird"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)  # Output: ['elephant', 'bird']