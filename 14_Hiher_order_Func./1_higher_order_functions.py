#  A higher-order function is a function that does at least one of the following:

# 1 Takes one or more functions as arguments.

# 2 Returns a function as its result.
# A function that takes another function as an argument
def greet(name):
    return f"Hello, {name}"

def speak(text, func):
    return func(text)

print(speak("Alice", greet))  # Output: Hello, Alice