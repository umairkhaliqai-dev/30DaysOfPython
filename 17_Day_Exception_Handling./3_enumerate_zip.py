# Enumerate: Adds a counter to an iterable and returns it as an enumerate object (useful to get index and value in a loop).

# Zip: Takes iterables (lists, tuples) and aggregates them into tuples, stopping at the shortest iterable.


# --- ENUMERATE ---
countries = ['Finland', 'Sweden', 'Norway']
print("--- Enumerate Example ---")
for index, country in enumerate(countries, start=1):
    print(f"{index}. {country}")

# --- ZIP ---
names = ['Asabeneh', 'Brook', 'David']
ages = [250, 30, 40]
print("\n--- Zip Example ---")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Zip to create a dictionary
countries_capitals = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm')]
for country, capital in countries_capitals:
    print(f"The capital of {country} is {capital}")