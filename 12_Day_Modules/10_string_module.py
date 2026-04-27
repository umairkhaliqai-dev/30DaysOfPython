# The string module contains useful string constants like all ASCII letters, digits, punctuation — handy for validation and generation.
import string

print(string.ascii_letters)   # abcdef...XYZ
print(string.digits)          # 0123456789
print(string.punctuation)     # !"#$%&'()*+,...)

# practical use — generate a random password
import random
chars = string.ascii_letters + string.digits
pwd = ''.join(random.choice(chars) for _ in range(8))
print(pwd)
print(random.choice(["Heads", "Tails"]))