# Definition: Anchors the match to the start of the string.

# Explanation: Inside square brackets ([^]), it means negation. Outside, it means "starts with".
import re 
text = "Python is great"
# Check if string starts with 'Py'
print(re.findall(r'^Py', text))   # Output: ['Py']
print(re.findall(r'^is', text))   # Output: [] (doesn't start with 'is')

# Negation inside brackets: match any non-digit
non_digits = re.findall(r'[^0-9]', 'abc123')
print(non_digits)  # Output: ['a', 'b', 'c']