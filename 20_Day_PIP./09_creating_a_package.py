# A Python package is a directory containing a special __init__.py file and other modules (.py files). You can organize your code into packages for reusability.
# Directory structure:
# mypackage/
#     __init__.py
#     greet.py
# In greet.py:
def say_hello(name):
    return f"Hello, {name}!"

# In another file:
# from mypackage import greet
# print(greet.say_hello("Student"))
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
print()
# For example 
from mypackage.arithmetic import add_numbers
from mypackage.greet import greet_person

print(add_numbers(5, 10, 20))
print(greet_person("Alice", "Smith"))
print()
# Database
# SQLAlchemy - Talks to any database (PostgreSQL, MySQL, SQLite) using Python objects

# Web Development
# Django - Everything-included web framework (Instagram uses it)

# Flask - Minimal, flexible web framework (you add what you need)

# HTML Parsing
# BeautifulSoup - Reads messy websites and extracts data

# PyQuery - Same job, but faster and uses jQuery-style syntax

# XML Processing
# ElementTree - Reads and writes XML files (comes with Python)

# GUI (Desktop Apps)
# PyQt - Professional desktop applications with native look

# Tkinter - Simple built-in GUI for basic tools

# Data Science & Machine Learning
# NumPy - Fast number crunching (the foundation)

# Pandas - Excel-like data tables in Python

# SciPy - Advanced math (algorithms, statistics, image processing)

# Scikit-learn - Ready-to-use machine learning models

# TensorFlow - Deep learning from Google

# Keras - Easier way to build neural networks (runs on TensorFlow)

# Networking
# Requests - Download web pages, call APIs, send data to servers