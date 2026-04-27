# Exercise 1: Age check for driving
print("=== Exercise 1: Driving Age Check ===")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print(f"You need {years_needed} more years to learn to drive.")
print()

# Exercise 2: Compare ages
print("=== Exercise 2: Age Comparison ===")
my_age = 25  # You can change this value
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print(f"I am {difference} year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age!")
print()

# Exercise 1: Grade Calculator
print("=== Exercise 1: Grade Calculator ===")
score = int(input("Enter your score: "))
if score > 100 or score < 0:
    print("Invalid score! Please enter a number between 0-100.")
elif score >= 90:
    grade = 'A'
    print(f"Your score {score} = Grade {grade}")
elif score >= 80:
    grade = 'B'
    print(f"Your score {score} = Grade {grade}")
elif score >= 70:
    grade = 'C'
    print(f"Your score {score} = Grade {grade}")
elif score >= 60:
    grade = 'D'
    print(f"Your score {score} = Grade {grade}")
else:
    print(f"Your score {score} = Grede F")
    print()
