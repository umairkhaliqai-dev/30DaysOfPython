# Definition: Matches the preceding character or group 0 or more times.

# Explanation: It will always match (because zero times is a match). Used when the pattern is optional but can appear many times.
import re 
text = "color colour colr"
# 'u' can appear 0 or more times
result = re.findall(r'colou*r', text)
print(result)  # Output: ['color', 'colour',]