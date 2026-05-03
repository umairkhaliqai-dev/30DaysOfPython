# EXERCISE 1: Filter negative and zero numbers
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)  

print()
# EXERCISE 2: Flatten a 2D list to 1D
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for sublist in list_of_lists for num in sublist]
print(flattened)  
print()
# Squares via List Comprehension
squares = [n**2 for n in range(1, 11)]
print(squares)
print()
# Filter with Comprehension
nums = [1, 2, 3, 4, 5,
       6, 7, 8, 9, 10]
div3 = [n for n in nums if n % 3 == 0]
print(div3)
# lamda function of adding 
def make_adder(n):
    return lambda x: x + n

add5  = make_adder(5)
add10 = make_adder(10)

print(add5(3))    
print(add10(7))   
print(add5(100))  

print()
#Given a list of words = ["apple", "banana", "fig", "kiwi", "elderberry"], use a list comprehension to return only the words that have more than 4 characters, and convert each to uppercase.

# Then write the same logic using a lambda + filter + map approach.
words = ["apple", "banana", "fig", "kiwi", "elderberry"]

# Method 1: List comprehension
result1 = [w.upper() for w in words if len(w) > 4]
print(result1)
# ['APPLE', 'BANANA', 'ELDERBERRY']

# Method 2: lambda + filter + map
filtered = filter(lambda w: len(w) > 4, words)
result2 = list(map(lambda w: w.upper(), filtered))
print(result2)
# ['APPLE', 'BANANA', 'ELDERBERRY']
