# Python has several built-in functions that act on other functions. The most famous are map(), filter(), and reduce(). They are efficient and commonly used in functional
# Using map in next file
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]