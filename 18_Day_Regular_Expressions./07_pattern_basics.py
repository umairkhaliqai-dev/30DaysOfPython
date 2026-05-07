# Definition: Using r'' (raw string notation) to write regex patterns so backslashes are treated literally.

# Explanation: Without r, you'd need to double escape (\\d). With r, it's natural (\d). Always use raw strings for regex.
# Without raw string (bad)
import re 
pattern1 = "\\d{3}"
# With raw string (good)
pattern2 = r"\d{3}"
text = "Code 123"
print(re.findall(pattern2, text))  # Output: ['123']
