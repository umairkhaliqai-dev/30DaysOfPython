print(" ==== Assignment Operator ==== ")
print(" Assignment Operator (=) is used to assign a value to a variable. It takes the value on the right side and stores it in the variable on the left side.")

name = "John"           # Assigns string "John" to variable name
age = 25                # Assigns number 25 to variable age
price = 19.99          # Assigns float 19.99 to variable price
is_student = True    #Assign boolean true to variable is_student
print("--- Example 1: Basic Assignment ---")
print("Name:", name)
print("Age:", age)
print("Price:", price)
print("Is student:", is_student)
print()

# Example 2: Multiple assignments in one line
x = y = z = 100        # Assigns 100 to x, y, and z all at once
a, b, c = 1, 2, 3      # Assigns 1 to a, 2 to b, 3 to c

print("--- Example 2: Multiple Assignments ---")
print("x =", x)
print("y =", y)
print("z =", z)
print("a =", a)
print("b =", b)
print("c =", c)
print()

# Reassigning values (overwriting)
print("--- Reassigning Values ---")
count = 10
print("Initial count:", count)

count = 25              # Old value 10 is replaced with 25
print("After reassignment:", count)

count = count + 5       # Using current value to create new value
print("After count + 5:", count) # I got answer 30 for this count.

# Practice: What will these output?
num = 50
print("\n--- Practice Test ---")
print("num =", num)

num = 100
print("After num = 100:", num)

num = num + 50
print("After num = num + 50:", num) # 150 Ans.
