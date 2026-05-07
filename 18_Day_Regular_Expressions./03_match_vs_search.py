# Definition: Several functions (match, search, findall, sub, split) that perform different regex operations.

# Explanation: Different methods serve different purposes: checking from start, searching anywhere, finding all, replacing, or splitting.
import re
text = "The rain in Spain"
# Different methods for different tasks
print(re.search('rain', text))  # Finds first occurrence
print(re.findall('ain', text))  # Finds all occurrences -> ['ain', 'ain']

print()
# re.match()
# Definition: Checks for a match only at the beginning of the string.

# Explanation: If the pattern is not found at index 0, it returns None (even if the pattern exists later in the string).
text = "Python is fun"
print(re.match('Python', text))  # Output: <re.Match object>
print(re.match('is', text))      # Output: None (not at beginning)

print()
# re.search()
# Definition: Scans through the entire string and returns the first match found anywhere.

# Explanation: Unlike match, it doesn't require the pattern to be at the start. It stops after the first match.
text = "Learn Python now"
result = re.search('Python', text)
print(result.group())  # Output: 'Python'
print(result.span())   # Output: (6, 12) - index positions