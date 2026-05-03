# This error is raised when you try to access an attribute (like a method or property) on an object that does not have that attribute. For example, trying to use a list method on a string.

text = "hello"
# ❌ Incorrect: Strings do not have an 'append' method
# text.append("!")

# ✅ Correct: Strings have a 'join' method
print(" ".join([text, "world"]))  # Output: hello world