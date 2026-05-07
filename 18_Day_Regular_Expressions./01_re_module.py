# Definition: A sequence of characters that forms a search pattern, mainly used for pattern matching with strings.

# Explanation: It's like a "mini-language" inside Python to find, extract, or replace specific text patterns (emails, phone numbers, etc.)

import re
pattern = "world"
text = "Hello world"
result = re.findall(pattern, text)
print(result)  # Output: ['world']