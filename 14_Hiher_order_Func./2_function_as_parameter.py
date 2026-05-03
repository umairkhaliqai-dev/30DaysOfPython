# This means passing a function (without calling it) into another function. The receiving function then calls that passed function internally.

def apply_operation(x, y, operation):
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))      # Output: 8
print(apply_operation(5, 3, multiply)) # Output: 15