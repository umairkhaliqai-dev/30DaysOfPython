# Unpacking extracts elements from iterables (lists, dicts) into variables using * or **. 
# Packing collects multiple arguments into a single variable (often using *args or **kwargs). 
# Spreading (* in Python) is similar to unpacking but used to expand iterables into function calls or literals.

# --- UNPACKING LISTS ---
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits  # Unpack into variables
print(f"x:{x}, y:{y}, z:{z}")

# --- UNPACKING DICTIONARIES ---
person = {'name': 'Alice', 'age': 30}
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(**person)  # Unpack dict into keyword arguments

# --- PACKING LISTS (*args)---
def sum_all(*numbers):  # Packs incoming arguments into a tuple
    return sum(numbers)
print(f"Packed sum: {sum_all(1,2,3,4)}")  # Output: 10

# --- PACKING DICTIONARIES (**kwargs)---
def print_data(**data):  # Packs into a dict
    for key, value in data.items():
        print(f"{key}: {value}")
print_data(name="Bob", job="Engineer")

# --- SPREADING (using * in lists)---
list1 = [1, 2]
list2 = [*list1, 3, 4]  # Spread list1 into new list
print(f"Spread list: {list2}")  # Output: [1, 2, 3, 4]

# Spreading into function arguments
numbers = [5, 6]
print(f"Spread into min: {min(*numbers)}")