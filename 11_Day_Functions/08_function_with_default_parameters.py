# Default values are used when the caller doesn't provide that argument.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # → Hello, Guest!
greet("Bob")      # → Hello, Bob!