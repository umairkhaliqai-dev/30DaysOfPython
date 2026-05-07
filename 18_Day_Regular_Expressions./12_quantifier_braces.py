# Definition: Curly braces specify exact number of repetitions for the preceding pattern.

# Explanation: {4} means exactly 4 times, {2,5} means 2 to 5 times, {3,} means 3 or more times.
import re 
text = "x xo xoo xooo xoooo"
# Exactly 2 'o's
print(re.findall(r'xo{2}', text))    # Output: ['xoo']

# 2 or 3 'o's
print(re.findall(r'xo{2,3}', text))  # Output: ['xoo', 'xooo']

# 8-digit numbers
ids = re.findall(r'\d{8}', 'ID: 12345678, 9876')
print(ids)  # Output: ['12345678']