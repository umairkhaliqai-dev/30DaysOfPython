# To create a decorator, you define a function that takes a function as an argument, defines a wrapper function inside it that adds the desired behavior, and returns the wrapper. We use the @ symbol syntax for convenience.

def uppercase_decorator(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Bob"))  # Output: HELLO, BOB