#  Six Digit/Character Random User ID
import random
import string

def random_user_id():
    """Generates a six digit/character random user ID."""
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id

# Test
print(random_user_id())  
print(random_user_id())  
print()
# RGB Color Generator
import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

print(rgb_color_gen())
print()
# userinput id form 
import random
import string

def user_id_gen_by_user():
    length = int(input("Number of characters: "))
    count  = int(input("Number of IDs: "))
    chars = string.ascii_letters + string.digits
    for _ in range(count):
        print(''.join(random.choice(chars) for _ in range(length)))

user_id_gen_by_user()

print()
# List of Hexadecimal Colors
import random

def list_of_hexa_colors(n):
    hex_chars = '0123456789abcdef'
    return ['#' + ''.join(random.choice(hex_chars) for _ in range(6))
            for _ in range(n)]

print(list_of_hexa_colors(3))