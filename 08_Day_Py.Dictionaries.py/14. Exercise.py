dog = {}
print("\n1. Empty dog dictionary:", dog)

# adding name ,color , breed etc..
dog['name'] = 'Max'
dog['color'] = 'Golden'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print("2. Dog dictionary after adding items:", dog)

# student dictionary:  
student = {
    'first_name': 'John',
    'last_name': 'Smith',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'React'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'}
print("\n3. Student dictionary:", student)

# len of student:
student_length = len(student)
print(f"\n4. Length of student dictionary: {student_length}")

# Get the value of skills and check the data type
skills_value = student['skills']
print(f"\n5. Skills value: {skills_value}")
print(f"5. Data type of skills: {type(skills_value)}")

# Modify the skills values by adding one or two skills
student['skills'].append('Django')
student['skills'].append('PostgreSQL')
print(f"\n6. Skills after adding more skills: {student['skills']}")

# Get the dictionary keys as a list
keys_list = list(student.keys())
print(f"\n7. Dictionary keys as list: {keys_list}")

 # Change the dictionary to a list of tuples using items() method
items_as_tuples = list(student.items())
print(f"\n Dictionary as list of tuples (first 3 items): {items_as_tuples[:3]}")
print(f" Total number of tuples: {len(items_as_tuples)}")

# Delete one of the items in the dictionary
removed_item = student.pop('marital_status')
print(f"\n10. Removed item 'marital_status' with value: {removed_item}")
print(f"10. Student dictionary after deletion: {student}")

# Delete one of the dictionaries
# We'll delete the 'dog' dictionary
print(f"\n11. Dog dictionary before deletion: {dog}")
del dog
print("11. Dog dictionary has been deleted!")
# print(dog)  # Uncommenting this would cause NameError: name 'dog' is not defined
try:
    print(dog)
except NameError:
 print("N/A")

# Bonus: Verify remaining dictionary
print("\n Final Student Dictionary:")
for key, value in student.items():
    print(f"   {key}: {value}")
    