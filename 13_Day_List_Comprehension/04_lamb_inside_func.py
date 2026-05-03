#Outer functions that return a lambda — creating reusable, configurable function factories. This pattern is the gateway to functional programming.
# Outer function returns a lambda
def multiplier(n):
    return lambda x: x * n

# Create specialized functions
double = multiplier(2)
triple = multiplier(3)
times_ten = multiplier(10)

print(double(5))     # 10
print(triple(5))     # 15
print(times_ten(5)) # 50
print()
#Power Genrator
def power(exp):
    return lambda base: base ** exp

square = power(2)
cube   = power(3)

print(square(4))   # 16
print(cube(3))     # 27

# Works with map() too
numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print(squares)
# [1, 4, 9, 16, 25]