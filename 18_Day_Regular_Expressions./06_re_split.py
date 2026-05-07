# Definition: Splits a string into a list, using a regex pattern as the delimiter.

# Explanation: More flexible than str.split() because you can split on multiple delimiters at once.
import re 
text = "apple, banana; orange grape|mango"
result = re.split(r'[,;| ]+', text)
print(result)  # Output: ['apple', 'banana', 'orange', 'grape', 'mango']