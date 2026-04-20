# Print the length of the company string using len() method and print().
company = "Passion to Code"
print(f"Length of string: {len(company)}") # it will be 15. 
print()

# Change all the characters to uppercase letters using upper() method.
print(company.upper())
print()

# Cut(slice) out the first word of Passion to Code string.
first_Word = company[0:7]
print(first_Word)
print()

# Check if Passion to Code string contains a word Passion using the method index, find or other methods.
company = "Passion to Code"
exist_word = "Passion"
if exist_word in company: 
    print(exist_word)
else:
    print("N/A")

    print()
    company = "Passion to Code"
# If it's NOT -1, it means the word exists
if company.find("Passion") != -1:
    print("Word exists!")
else:
    print("N/A")

print()
company = "Passion to Code"

try:
    position = company.index("Passion")
    print(f"Found at index: {position}")
except ValueError:
    print("N/A")
print()
#Replace the word Passion in the string 'Passion to Code' to Python.
New_string = company.replace('Passion', 'Pyhton')
print(New_string)
print()
# Split the string 'Passion to code' using space as the separator (split()) .
print(company.split(' '))
print()
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"
acronym = ''.join(word[0] for word in phrase.split())
print(f"Acronym: {acronym}")
print()
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
old_phrase = 'You cannot end a sentence with because because because is a conjunction'
new_phrase = old_phrase[30:54] #Not Recommended as it works only on this sentence. 
print(new_phrase)
print()
sentence = 'You cannot end a sentence with because because because is a conjunction'
result = sentence[sentence.find('because'):sentence.rfind('because')+7]
print(result)  # Output: because because because
print()
sentence = 'You cannot end a sentence with because because because is a conjunction'

# Method 1: Using find() and rfind() (Most Reliable)
start = sentence.find('because')
end = sentence.rfind('because') + len('because')  # +7 to include last 'because'
result = sentence[start:end]
print(result)  # Output: because because because
print()
#Does 'Coding For All' start with a substring Coding?
phrase = 'Coding for all'
start_word = phrase.startswith('Coding')
print(start_word)
print()

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
unform = '  Coding for all    '
print(unform.strip())
print()
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pyhton_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " # ".join(pyhton_lib)
print(result)
print()
# use of tab escape 
# Using \t to create tab-separated columns
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")