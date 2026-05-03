# This error occurs when you try to import a module using the import statement, but Python cannot locate that module in its search path or installed libraries.


# ❌ Incorrect: 'numpy' is not installed or 'nump' is a typo
# import nump

# ✅ Correct: Import a built-in or installed module correctly
import math
print(math.sqrt(16))  # Output: 4.0