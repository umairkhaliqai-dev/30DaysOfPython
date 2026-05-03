# reduce(function, sequence) (from the functools module) applies a rolling computation to sequential pairs of values in a list. It reduces the sequence to a single value.

from functools import reduce

# Calculate the product of all numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (Calculation: 1*2=2, 2*3=6, 6*4=24)

# Find the maximum number
max_num = reduce(lambda x, y: x if x > y else y, [47, 11, 42, 102, 13])
print(max_num)  # Output: 102
