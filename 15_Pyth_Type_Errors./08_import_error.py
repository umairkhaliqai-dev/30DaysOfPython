# This error occurs when the import statement successfully finds the module, but a specific function, class, or variable you tried to import from that module does not exist. It's a more specific version of ModuleNotFoundError.
from math import power  # ❌ Incorrect: 'power' does not exist in math
# Correct:
# from math import pow
from math import pow
print(pow(2, 3))  # Output: 8.0