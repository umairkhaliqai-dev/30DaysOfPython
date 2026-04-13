full_name = "Umair Khalid"
age = 25
is_married = False
is_light_on = True
print(f"Type of full_name: {type(full_name)}")
print(f"Type of age: {type(age)}")
print(f"Type of is_married: {type(is_married)}")
print(f"Type of is_light_on: {type(is_light_on)}\n")
print("=== EXERCISE 2: Length of Full Name ===\n")
full_name_length = len(full_name)
print(f"My full name '{full_name}' has {full_name_length} characters\n")
print("=== EXERCISE 4: Declare Variables ===\n")
num_one = 5
num_two = 4
print(f"num_one = {num_one}")
print(f"num_two = {num_two}\n")
print("=== EXERCISES 5-11: Math Operations ===\n")
total = num_one + num_two
print(f"Addition ({num_one} + {num_two}) = {total}")
division = num_one / num_two
print(f"Division ({num_one} ÷ {num_two}) = {division}")
remainder = num_two % num_one
print(f"Modulus ({num_two} % {num_one}) = {remainder}")
exp = num_one ** num_two
print(f"Exponential ({num_one} ^ {num_two}) = {exp}")
floor_division = num_one // num_two
print(f"Floor Division ({num_one} // {num_two}) = {floor_division}\n")
print("=== EXERCISE 12: Circle Calculations ===\n")
radius = 30
area_of_circle = 3.14159 * (radius ** 2)
circum_of_circle = 2 * 3.14159 * radius

print(f"Radius: {radius} meters")
print(f"i. Area of circle: {area_of_circle:.2f} square meters")
print(f"ii. Circumference of circle: {circum_of_circle:.2f} meters")
print("\n--- Part iii: User Input ---")
user_radius = float(input("Enter the radius of the circle: "))
user_area = 3.14159 * (user_radius ** 2)
print(f"Area of circle with radius {user_radius} is: {user_area:.2f} square units\n")
# Exercise 13: Get user information
print("=== EXERCISE 13: User Information ===\n")

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

print("\n--- Your Information ---")
print(f"First Name: {user_first_name}")
print(f"Last Name: {user_last_name}")
print(f"Country: {user_country}")
print(f"Age: {user_age}\n")

help("keywords")


import keyword
print("Python Reserved Keywords:")
print(keyword.kwlist)

