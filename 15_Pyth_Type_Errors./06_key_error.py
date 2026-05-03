# This error happens when you try to access a key in a dictionary that does not exist in that dictionary.

person = {"name": "Alice", "age": 30}
# ❌ Incorrect: The key 'city' does not exist
# print(person["city"])

# ✅ Correct: Access existing key or use .get()
print(person.get("city", "Unknown"))  # Output: Unknown
print(person["name"])                 # Output: Alice
