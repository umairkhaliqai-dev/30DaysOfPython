print(" ==== 📐 Arithmetic Operator ==== ")
print("Arithmetic Operators are used to perform mathematical operations on numbers. They work just like basic math calculations (addition, subtraction, multiplication, division, etc.)")
# Example 1: Basic Arithmetic Operations
print("=" * 40)  # this command help me to create a margin line above title.
print("EXAMPLE 1: BASIC ARITHMETIC")
print("=" * 40) # similarly this command line gave a margin line below the title. 

# Declare variables
num1 = 15
num2 = 4

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

# Display results
print(f"Numbers: {num1} and {num2}")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus} (remainder)")
print(f"{num1} ** {num2} = {exponentiation} (15 to the power of 4)")
print(f"{num1} // {num2} = {floor_division} (integer division)")
print("\n")

s = "hello"
t = s
s = s.upper()
print(t)

# 1. Create a list (Mutable)
s = ["h", "e", "l", "l", "o"]
t = s  # t now points to the exact same list object

# 2. Modify the content of the list 'in-place'
# We loop through the list and change each letter to uppercase
for i in range(len(s)):
    s[i] = s[i].upper()

# 3. Check the result
print(f"s: {s}")
print(f"t: {t}")

x = 4
while x < 10:
    x*= x/2
print(x)

# Real world calculation. 
print("=" * 40)
print("Real Claculation")
print("=" * 40)

food_bill = 37.67 # £
Tip_Percentage = 15 # % Tip
Tip_amount = food_bill * (Tip_Percentage/100)
Total_Bill = food_bill + Tip_amount

print("----- Restaurant Bill-----")
print(f"\n Food Bill: £{food_bill}")
print (f"Tip {Tip_Percentage}%: £{Tip_amount:.2f}")
print(f"Total Bill: £{Total_Bill:.2f}")
print("Thank You ╾━╤デ╦︻ (•_- )")


# Example 2: Real-World Arithmetic Applications
print("=" * 40)
print("EXAMPLE 2: REAL-WORLD CALCULATIONS")
print("=" * 40)

# Calculate total bill with tip
meal_cost = 45.50
tip_percentage = 15  # 15% tip
tip_amount = meal_cost * (tip_percentage / 100)
total_bill = meal_cost + tip_amount

print("💰 RESTAURANT BILL CALCULATOR")
print(f"Meal cost: ${meal_cost}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Total bill: ${total_bill:.2f}")
print()

# Real world calculation. 
print("=" * 40)
print("Real Claculation")
print("=" * 40)

food_bill = 37.67 # £
Tip_Percentage = 15 # % Tip
Tip_amount = food_bill * (Tip_Percentage/100)
Total_Bill = food_bill + Tip_amount

print("----- Restaurant Bill-----")
print(f"\n Food Bill: £{food_bill}")
print (f"Tip {Tip_Percentage}%: £{Tip_amount:.2f}")
print(f"Total Bill: £{Total_Bill:.2f}")
print()
print("Thank You ╾━╤デ╦︻ (•_- )")
print()

# Calculate average score
scores = [85, 92, 78, 90, 88]
total_score = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]
number_of_tests = len(scores)
average_score = total_score / number_of_tests

print("📊 GRADE CALCULATOR")
print(f"Test scores: {scores}")
print(f"Total points: {total_score}")
print(f"Number of tests: {number_of_tests}")
print(f"Average score: {average_score:.1f}%")
print()


# Calculate with exponentiation (compound interest example)
principal = 1000  # $1000
rate = 0.05       # 5% annual interest
years = 3
compound_interest = principal * (1 + rate) ** years

print("💰 COMPOUND INTEREST")
print(f"Principal: ${principal}")
print(f"Annual rate: {rate * 100}%")
print(f"Years: {years}")
print(f"Total after {years} years: ${compound_interest:.2f}")


# Challenge: Can you predict the output?
print("\n" + "=" * 40)
print("QUICK CHALLENGE")
print("=" * 40)

a = 25
b = 7

print(f"a = {a}, b = {b}")
print(f"a + b * 2 = {a + b * 2}")        # Which happens first?
print(f"(a + b) * 2 = {(a + b) * 2}")    # Different result!
print(f"a % b = {a % b}")                # Remainder when 25 ÷ 7
print(f"a // b = {a // b}")              # How many full times?


# MODIFICATION 1: Different interest rates
print("\n" + "="*40)
print("COMPARING INTEREST RATES")
print("="*40)

principal = 1000
years = 5

for rate in [0.03, 0.05, 0.07, 0.10]:
    final = principal * (1 + rate) ** years
    print(f"{rate*100}% interest: ${final:.2f}")

print("WRONG")
principal = 1000
rate = 0.05
years = 3

wrong = principal * (2 + rate ** years)  # 1000 × (0.05³)
print(wrong)  # $0.125 (just 12.5 cents!)


print("=" * 50)
print("WHY WE NEED 1 + rate")
print("=" * 50)

principal = 1000
rate = 0.05
years = 3

# WRONG: Only calculates interest growth
interest_only = principal * (rate ** years)
print(f"WRONG: Interest only: ${interest_only:.2f}")
print("(This only grows the interest rate itself, not the money!)")
print()

# RIGHT: Calculates total money growth
total_money = principal * (1 + rate) ** years
print(f"RIGHT: Total money: ${total_money:.2f}")
print("(This grows YOUR MONEY + interest each year)")
print()

# VERIFICATION: Manual calculation
print("VERIFICATION - Manual year by year:")
money = principal
for year in range(1, years + 1):
    interest = money * rate
    money = money + interest  # This is where we ADD to original
    print(f"Year {year}: ${money:.2f} (Added ${interest:.2f} interest)")

print(f"\nFinal total matches: ${money:.2f}")




print("=" * 60)
print("TESTING DIFFERENT NUMBERS INSTEAD OF 1")
print("=" * 60)

principal = 1000
rate = 0.05  # 5% interest
years = 3

print(f"Starting with: ${principal}")
print(f"Interest rate: {rate*100}%")
print(f"Years: {years}")
print()

# Using 1 (CORRECT)
correct = principal * (1 + rate) ** years
print(f"✓ Using 1: ${correct:.2f}")
print("  Formula: principal × (1 + 0.05)³")
print("  Meaning: 100% of money + 5% interest")
print()

# Using 2 (WRONG - doubles your money every year!)
wrong_with_2 = principal * (2 + rate) ** years
print(f"✗ Using 2: ${wrong_with_2:.2f}")
print("  Formula: principal × (2 + 0.05)³ = 1000 × 2.05³")
print("  Problem: This assumes 200% of money + 5% interest")
print("  Result: Artificially doubles money each year!")
print()

# Using 0.5 (WRONG - loses half your money!)
wrong_with_0_5 = principal * (0.5 + rate) ** years
print(f"✗ Using 0.5: ${wrong_with_0_5:.2f}")
print("  Formula: principal × (0.5 + 0.05)³ = 1000 × 0.55³")
print("  Problem: This assumes only 50% of money remains")
print("  Result: Loses half your principal immediately!")
print()

# Demonstration of why 1 is universal
print("=" * 60)
print("WHY 1 IS THE ONLY CHOICE")
print("=" * 60)

print("Year-by-year breakdown with 1:")
money = 1000
for year in range(1, 4):
    interest = money * 0.05
    money = money + interest  # Notice: adding to original!
    print(f"Year {year}: ${money:.2f} = ${money/1000:.2f} × original")
    print(f"         Multiplier: {money/1000:.2f}")

print("\nThe multiplier after 3 years is 1.157625")
print("This equals (1.05)³ = (1 + 0.05)³")
print("The '1' keeps your original money INTACT while adding growth")




