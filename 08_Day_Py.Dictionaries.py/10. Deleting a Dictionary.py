person = {"name": "Bob", "age": 25, "country": "Canada"}
del person
try:
    print(person)
except NameError:
    print('N/A')
    