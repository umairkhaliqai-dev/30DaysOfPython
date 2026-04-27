# 1. Iterate 0 to 10 using for loop
print("For loop 0 to 10:")
for i in range(11):
    print(i, end=" ")
print("\n")
# Iterate 0 to 10 using while loop
print("While loop 0 to 10:")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")
# Iterate 10 to 0 using for loop
print("For loop 10 to 0:")
for i in range(10, -1, -1):
    print(i, end=" ")
print("\n")
# Iterate 10 to 0 using while loop
print("While loop 10 to 0:")
i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1
print("\n")

# 3. Triangle pattern using loop
print("Triangle pattern:")
for i in range(1, 8):
    print("#" * i)

# 8x8 square pattern using nested loops
print("\n8x8 Square pattern:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
    # 5. Multiplication table pattern
print("\nMultiplication table:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")
    # 2. Sum of all evens and odds from 0 to 100
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"The sum of all evens is: {sum_evens}")
print(f"The sum of all odds is: {sum_odds}")
# Output: sum_evens = 2550, sum_odds = 2500

# 2. Reverse fruit list using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

print(f"\nOriginal list: {fruits}")
# Method 1: Using reverse loop
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(f"Reversed list: {reversed_fruits}")
# Output: ['lemon', 'mango', 'orange', 'banana']