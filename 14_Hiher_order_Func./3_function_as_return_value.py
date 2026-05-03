# A function that returns another function. The returned function can "remember" the environment in which it was created (this leads to closures).

def power_generator(exp):
    def power(base):
        return base ** exp
    return power

square = power_generator(2)
cube = power_generator(3)

print(square(5))  # Output: 25
print(cube(5))    # Output: 125