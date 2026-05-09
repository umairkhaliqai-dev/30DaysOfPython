# The __init__() method is automatically called when an object is created. It initializes the object's attributes.
class Person:
    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age

p = Person("Alice", 25)
print(p.name, p.age)  # Alice 25
print()
# Explanation: Methods are functions defined inside a class that describe the behaviors of an object.
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):  # Object method
        return f"{self.name} says Woof!"

dog = Dog("Rex")
print(dog.bark())  # Rex says Woof!
print()
# Default methods like __str__ control how an object is displayed (e.g., when printed). Without them, printing an object shows a memory address.
class Book:
    def __init__(self, title):
        self.title = title
    
    def __str__(self):  # Default method for string representation
        return f"Book: {self.title}"

book = Book("1984")
print(book)  # Book: 1984 (instead of <__main__.Book object at 0x...>)
print()
#Explanation: Use class methods (with @classmethod) to modify class-level attributes that are shared across all instances.

class Emp:
    company = "Old Corp"  # Class default value
    
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

print(Emp.company)  # Old Corp
Emp.change_company("New Tech")
print(Emp.company)  # New Tech