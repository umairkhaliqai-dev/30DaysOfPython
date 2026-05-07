# Definition: Returns a list of all non-overlapping matches of the pattern in the string.

# Explanation: If there are multiple matches, it captures all of them. If no matches, returns an empty list.
import re 
text = "My numbers are 10, 20, and 30"
all_numbers = re.findall(r'\d+', text)
print(all_numbers)  # Output: ['10', '20', '30']