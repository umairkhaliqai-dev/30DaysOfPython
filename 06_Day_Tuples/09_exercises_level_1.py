# Empty tuple using parentheses
empty_tuple = ()
print("Empty tuple:", empty_tuple)
print("Type:", type(empty_tuple))

# Alternative using tuple() constructor
empty_tuple_alt = tuple()
print("Alternative empty tuple:", empty_tuple_alt)

# Tuple of sisters (imaginary names)
sisters = ("maryam", "ayesha", "Meera")
print("Sisters:", sisters)

# Tuple of brothers (imaginary names)
brothers = ("ali", "arham", "zain")
print("Brothers:", brothers)

# Join using + operator
siblings = sisters + brothers
print("All siblings:", siblings)

# Using len() function
sibling_count = len(siblings)
print("Number of siblings:", sibling_count)  

# Alternative: Directly print
print(f"I have {len(siblings)} siblings")

# Exercise 5: Add parents to create family_members
siblings_list = list(siblings)
siblings_list.append("Abdullah")   # Father
siblings_list.append("Fatima")   # Mother
family_members = tuple(siblings_list)
print("5. Family members:", family_members)
print("   Total family members:", len(family_members))

