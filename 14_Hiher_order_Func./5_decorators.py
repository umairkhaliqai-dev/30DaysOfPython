# Decorators are a powerful design pattern that allows you to add new functionality to an existing function without modifying its structure. A decorator is a function that takes another function and extends its behavior.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function.")
        func()
        print("Something is happening after the function.")
    return wrapper

def say_hello():
    print("Hello!")

# Applying decorator
say_hello = my_decorator(say_hello)
say_hello()
print()
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
