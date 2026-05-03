# The patterns you'll see most often — zero args, one arg, multiple args, and conditional expressions inside a lambda.
# 1. Zero arguments
greet = lambda: "Hello, World!"
print(greet())
# Hello, World!
print()
# 2. One argument
double = lambda x: x * 2
print(double(9))
# 18
print()
# 3. Multiple arguments
full_name = lambda first, last: first + " " + last
print(full_name("Asabeneh", "Yetayeh"))
# Asabeneh Yetayeh
print()
# 4. Conditional expression (inline if/else)
is_even = lambda n: "even" if n % 2 == 0 else "odd"
print(is_even(7))
# odd
print(is_even(10))
# even
# Calling Lambda Immediately (IIFE)
#You can call a lambda immediately without assigning it to a variable — wrap it in parentheses and call it right away. This is called an Immediately Invoked Function Expression.

 # Assign, then call
cube = lambda x: x ** 3
print(cube(4))   # 64

# Call immediately without assigning
result = (lambda x: x ** 3)(4)
print(result)    # 64