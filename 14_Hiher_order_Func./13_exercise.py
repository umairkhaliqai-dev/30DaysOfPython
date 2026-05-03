#  Explain the difference between map, filter, and reduce.
# Simple explanation:

# map() - Transforms EVERY item in a list (like giving everyone a birthday gift )

# filter() - Selects ONLY SOME items based on a condition (like a bouncer at a club )

# reduce() - Combines ALL items into ONE single value (like adding all numbers )

print()
# Explain the difference between higher order function, closure and decorator
# Concept	What it is	Simple Analogy
# Higher Order Function	A function that takes or returns another function	A factory that makes tools 
# Closure	A function that remembers variables from where it was created	A backpack that carries memories 
# Decorator	A special higher order function that modifies another function	A photo filter that changes pictures 
print()
# for loops: 
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print each country
for country in countries:
    print(country)

# Print each name
for name in names:
    print(name)

# Print each number
for number in numbers:
    print(number)
print()
# higher order functions now :
print()
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Map to uppercase countries
countries_upper = list(map(str.upper, countries))
print(countries_upper)

# 2. Map to square numbers
numbers_squared = list(map(lambda x: x**2, numbers))
print(numbers_squared)

# 3. Map to uppercase names
names_upper = list(map(str.upper, names))
print(names_upper)

# 4. Filter countries containing 'land'
land_countries = list(filter(lambda country: 'land' in country, countries))
print(land_countries)  # ['Finland', 'Iceland']

# 5. Filter countries with exactly six characters
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_char_countries)  # ['Sweden']

# 6. Filter countries with six letters OR more
six_or_more = list(filter(lambda country: len(country) >= 6, countries))
print(six_or_more)  # ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Iceland']

# 7. Filter countries starting with 'E'
e_countries = list(filter(lambda country: country.startswith('E'), countries))
print(e_countries)  # ['Estonia']

# 8. Chain map, filter, reduce together
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
print(result)  # Sum of squares of even numbers: 2²+4²+6²+8²+10² = 220

# 9. Function to get only string items from a list
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

mixed = [1, 'hello', 2, 'world', 3.5, 'python']
strings_only = get_string_lists(mixed)
print(strings_only)  # ['hello', 'world', 'python']

# 10. Reduce to sum all numbers
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)  # 55

# 11. Reduce to create sentence
sentence = reduce(
    lambda x, y: x + ', ' + y,
    countries[:-1]  # All except last
) + f', and {countries[-1]} are north European countries'
print(sentence)
# Output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# 12. Function to categorize countries by pattern
def categorize_countries(pattern):
    # Using the countries list from earlier
    return [country for country in countries if pattern in country.lower()]

print(categorize_countries('land'))  # ['Finland', 'Iceland']
print(categorize_countries('ia'))    # ['Estonia']

# 13. Dictionary with starting letters as keys
def country_letter_count(country_list):
    letter_count = {}
    for country in country_list:
        first_letter = country[0]
        if first_letter in letter_count:
            letter_count[first_letter] += 1
        else:
            letter_count[first_letter] = 1
    return letter_count

print(country_letter_count(countries))
# {'E': 1, 'F': 1, 'S': 1, 'D': 1, 'N': 1, 'I': 1}



