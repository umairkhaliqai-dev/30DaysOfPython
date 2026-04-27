# Same logic as while, but used inside a for loop.
# Example: Stop if 'banana' is found (Break) or Skip 'banana' (Continue)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)  # Only prints 'apple'

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)  # Prints 'apple', 'cherry' (skipped banana)
