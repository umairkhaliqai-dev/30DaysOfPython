sisters = ("maryam", "ayesha", "Meera")
brothers = ("ali", "arham", "zain")
siblings = sisters + brothers
siblings_list = list(siblings)
siblings_list.append("Ahmed")   # Father
siblings_list.append("shazia")   # Mother
family_members = tuple(siblings_list)
# Unpacking: First 6 are siblings, last 2 are parents
*siblings_unpacked, father, mother = family_members
print("Siblings:", siblings_unpacked)
print("Father:", father)
print("Mother:", mother)

# Alternative method using slicing
siblings_slice = family_members[:-2]
parents = family_members[-2:]
print("\nAlternative - Siblings:", siblings_slice)
print("Alternative - Parents:", parents)

# Create three separate tuples
fruits = ("Apple", "Banana", "Orange", "Mango", "Grapes")
vegetables = ("Carrot", "Broccoli", "Spinach", "Tomato")
animal_products = ("Milk", "Eggs", "Cheese", "Yogurt")

# Join all three tuples
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)
print("Length of food tuple:", len(food_stuff_tp))

# Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)
print("Type:", type(food_stuff_lt))  # <class 'list'>

# Find middle index
length = len(food_stuff_lt)
middle_index = length // 2

# If length is odd, one middle item; if even, two middle items
if length % 2 == 1:
    # Odd length - one middle item
    middle_items = food_stuff_lt[middle_index]
    print(f"Tuple has {length} items (odd)")
    print(f"Middle item at index {middle_index}: {middle_items}")
else:
    # Even length - two middle items
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
    print(f"Tuple has {length} items (even)")
    print(f"Middle two items: {middle_items}")

# Example output for our 12 items (even): ('Mango', 'Carrot')
# First three items
first_three = food_stuff_lt[:3]
print("First three items:", first_three)

# Last three items
last_three = food_stuff_lt[-3:]
print("Last three items:", last_three)

# Alternative: Last three using length
last_three_alt = food_stuff_lt[len(food_stuff_lt)-3:]
print("Last three (alternative):", last_three_alt)


# Delete the entire tuple
del food_stuff_tp

# Verify it's deleted
try:
    print(food_stuff_tp)
except NameError:
    print("food_stuff_tp has been successfully deleted!")
    print("NameError: name 'food_stuff_tp' is not defined")

    nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
countries_to_check = ['Estonia', 'Iceland']
for country in countries_to_check:
    if country in nordic_countries:
        print(f"✓ {country} IS a Nordic country")
    else:
        print(f"✗ {country} is NOT a Nordic country")
