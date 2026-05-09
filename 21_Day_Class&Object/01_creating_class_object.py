# A class is a blueprint for creating objects (a particular data structure), and an object is an instance of a class. Think of a class as a "cookie cutter" and objects as the "cookies".
# Class definition
class Car:
    pass

# Creating objects (instances)
toyota = Car()
bmw = Car()
print(type(toyota))  # <class '__main__.Car'>
print()
#Use the class keyword to define a class. Instantiate an object by calling the class like a function.
class Student:
    school = "Python High"  # Class attribute

# Creating objects
student1 = Student()
student2 = Student()
print(student1.school)  # Python High