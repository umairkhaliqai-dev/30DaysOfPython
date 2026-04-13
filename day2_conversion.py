number_str = "250"
number_int = int(number_str)
print(f"Original: {number_str} (Type: {type(number_str)})")
print(f"converted: {number_int} (Type: {type(number_int)})")
print(f"math operation: {number_int} +10 = {number_int +10}\n")

price_str = "19.99"
price_float = float(price_str)
print(f"Price as text: {price_str}")
print(f"Price as number: {price_float}")
print(f"With tax (10%): ${price_float * 1.10}\n")

print("\n--- Multiple inputs on one line ---")
data = input("Enter your name and age (separated by space): ")
parts = data.split()
if len(parts) == 2:
    person_name = parts[0]
    person_age = parts[1]
    print(f"Name: {person_name}, Age: {person_age}") 