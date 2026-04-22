person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("1. Original Dict:", person)

# pop() removes and returns the value. popitem() removes the last item.
removed_city = person.pop("city")
print(" Removed 'city':", removed_city)
print(" Dict after pop:", person)
