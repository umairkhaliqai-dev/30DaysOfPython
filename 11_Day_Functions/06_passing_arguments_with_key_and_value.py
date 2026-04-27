# Keyword arguments let you pass values by name, making the call more readable and order-independent.
def introduce(name, age):
    print(f"I am {name}, age {age}")

introduce(age=25, name="Alice")
# → I am Alice, age 25