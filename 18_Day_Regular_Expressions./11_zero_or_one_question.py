# Definition: Matches the preceding character or group 0 or 1 time (makes it optional).

# Explanation: The pattern might or might not be there, but if it is there, it can appear only once.
import re 
text = "color colour"
# 'u' appears 0 or 1 time
result = re.findall(r'colou?r', text)
print(result)  # Output: ['color', 'colour']