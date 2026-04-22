person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("1. Original Dict:", person)

# items() returns a view of key-value pairs as tuples.
items_list = list(person.items())
print(" List of Tuples:", items_list)  # e.g., [('name', 'Alice'), ('age', 31)]