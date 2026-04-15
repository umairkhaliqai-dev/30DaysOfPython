# 4 calculating Triangle area
print("=" * 30)
print("Triangle Area")
print("=" * 30)
print()
Base = float(input("enter Base:"))
Height = float(input("enter Height:"))
Area = 0.5 * Base * Height
print(f"The area of Triangle is:{Area}\n")

# 7 Area & circumference of Circle calculation.
print("=" * 30)
print("Circle Area & Circumference")
print("=" * 30)
print()
Radius = float(input("enter Radius: \n"))
Area = 3.14159 * Radius * Radius
Circumference = 2 * 3.14159 * Radius
print()
print(f"The area of circle is {Area:.2f}")
print(f"The circumference of circle is {Circumference:.2f} \n")

# 11 Find x where y = x**2 + 6x + 9 = 0
print("=" * 30)
print("Quadratic Equation")
print("=" * 30)
print()
print("Eq: y = x**2 + 6x + 9")
print("Find x where y = 0 \n")
for x in range (-7, 7):
 y = x**2 + 6*x + 9
if y == 0:
 print(f"when x = {x}, y = {y}")

# 13 Check if "on" is in both "python" and "dragon"
print("=" * 40)
print(" in operator with and")
print("=" * 40)
word1 = "pyhton"
word2 = "dragon"
check_on = "on" in word1 and "on" in word2
print(f"is on in {word1}?, yes on in {word1}")
print(f"is on in {word2}?, yes on in {word2}")
print()

print()
# 16 Type conversion chain system.
print("=" * 30)
print("Type conversion chain")
print("=" * 30)

Text = "python"
length = len(Text)
Length_float = float(length)
Length_string = str(Length_float)

print(f"\n Original Text: {Text} | Type: {type(Text)}")
print(f"length (int): {length} | Type: {type(length)}")
print(f"\n Float convert is {Length_float} | Type: {type(Length_float)}")
print(f"string convert: {Length_string} | Type: {type(Length_string)}\n")

print()
# 17 Even Number Checker.
print("=" * 50)
print("Even Number Checker")
print("=" * 50)

user_number = int(input("enter any number"))
if user_number % 2 == 0:
 print(f" The {user_number} is Even as the remainder is 0 when divided by 2")
else: 
 print(f" The {user_number} is ODD as the remainder is {user_number % 2} when divided by 2")

print()
 # 21 Calculating Real world salary.
print("=" * 30)
print("Weekly Salary")
print("=" * 30) 
Hours = float(input("\n Enter Hours worked: "))
Rate = float(input("Enter Your /Hour rate: £"))
weekly_earning = Hours * Rate
print(f"\n Congratulations 🃏! Your salary for this week is £{weekly_earning} \n")








 