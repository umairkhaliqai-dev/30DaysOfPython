# Definition: Replaces occurrences of a pattern in a string with a new substring.

# Explanation: Takes three main args: pattern, replacement, string. It's like str.replace() but with regex power.
import re 
text = "I like blue car"
new_text = re.sub('blue', 'red', text)
print(new_text)  # Output: "I like red car"