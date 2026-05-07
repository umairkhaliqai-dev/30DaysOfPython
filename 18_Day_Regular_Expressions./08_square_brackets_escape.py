# Definition: Used to specify a set of characters you wish to match (e.g., [aeiou] matches any vowel).

# Explanation: Matches any single character inside the brackets. Ranges like [a-z] (lowercase) or [0-9] (digits) are common.
import re 
text = "cat bat rat mat"
vowels = re.findall(r'[aeiou]', text)
print(vowels)  # Output: ['a', 'a', 'a', 'a']

digits = re.findall(r'[0-5]', 'Room 404')
print(digits)  # Output: ['4', '0', '4']
print()
#Escape Character \ in RegEx
# Definition: Used to escape a metacharacter (like ., *, +, ?, [], etc.) to match it literally.

# Explanation: If you want to find a literal period or asterisk, you must escape it with a backslash.
text = "The price is $19.99"
# Without escape: '.' matches ANY character
print(re.findall(r'19.99', text))  # Output: ['19.99'] (works because '.' matches the dot)

# To match actual dot:
print(re.findall(r'\$19\.99', text))  # Output: ['$19.99']

# Matching a dollar sign:
price = re.findall(r'\$', text)
print(price)  # Output: ['$']

print()
# Definition: Matches the preceding character or group 1 or more times (as many as possible).

# Explanation: Will match if the pattern appears at least once. Equivalent to {1,}.
text = "abc abbc abbbc aaaaa"
result = re.findall(r'ab+c', text)  # 'b' one or more times
print(result)  # Output: ['abc', 'abbc', 'abbbc']
print()
#  Period .
# Definition: Matches any single character except newline (\n).

# Explanation: The wildcard of regex. Very powerful but use carefully because it matches almost everything.
text = "cat hat bat 123 "
# Matches any three-character sequence starting with 'c'
result = re.findall(r'c..', text)   # 'c' + any 2 chars
print(result)  # Output: ['cat']

# Matches any four characters
any_four = re.findall(r'....', text)
print(any_four)  # Output: ['cat ', 'hat ', 'bat ', '123']