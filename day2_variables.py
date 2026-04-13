first_name ="Umair"
last_name = "Khaliq"
print("My Information:")
print(f"My Name is:{first_name , last_name}")
print(f"Type of first_name: {type(first_name)}")
x=y=z=100
print(f"same value: x={x} , y={y}, z={z}")
data = input("Enter name and age: ")
parts = data.split()

for item in parts:
    print(item)
    print("") # This prints an empty line to create the "bottom" effect