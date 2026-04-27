# Core idea: Check multiple conditions in sequence.


score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This runs (85 is between 80 and 89)
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

