# Use del keyword. Warning: This completely deletes the tuple variable.
temp_tuple = (1, 2, 3)
del temp_tuple
# Next line would raise NameError because tuple is gone
# print(temp_tuple)  # NameError: name 'temp_tuple' is not defined
print(temp_tuple) # error of name 