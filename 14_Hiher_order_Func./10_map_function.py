# map(function, iterable) applies a given function to every item in an iterable (like a list or tuple) and returns a map object (which can be converted to a list).
# Convert a list of strings to integers
str_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, str_nums))
print(int_nums)  # Output: [1, 2, 3, 4]

# Using lambda
nums = [2, 4, 6, 8]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)   # Output: [4, 8, 12, 16]
