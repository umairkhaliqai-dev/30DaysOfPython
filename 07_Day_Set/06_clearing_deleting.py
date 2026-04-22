# If we want to clear or empty the set we use clear method.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

# If we want to delete the set itself we use del operator.
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

try:
    # Indented 4 spaces
    print(fruits) 
except NameError:
    # Indented 4 spaces
    print('The variable "fruits" does not exist (N/A)')  # I need to uese Try box for except function and need to give proper indentations.
    







