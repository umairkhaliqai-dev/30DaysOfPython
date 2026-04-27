# Functions are first-class objects in Python — you can pass one function into another.
def double(n):
    return n * 2

def apply(func, value):
    return func(value)

print(apply(double, 5))  # → 10