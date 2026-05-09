# Explanation: Inheritance allows a class (child) to inherit attributes and methods from another class (parent), promoting code reuse.

class Animal:  # Parent class
    def speak(self):
        return "Some sound"

class Cat(Animal):  # Child inheriting from Animal
    pass

cat = Cat()
print(cat.speak())  # Some sound (inherited method)
print()
# Explanation: A child class can provide a specific implementation of a method that is already defined in its parent class.

class Animal:
    def speak(self):
        return "Generic sound"

class Cat(Animal):
    def speak(self):  # Overriding parent method
        return "Meow!"

class Dog(Animal):
    def speak(self):
        return "Woof!"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())  # Meow! Woof!