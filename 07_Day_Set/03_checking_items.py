# Sets have no index, so you loop through them.
# Sets are unordered – you cannot index. Use a loop.
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
# Output order may vary: banana, cherry, apple etc.
# To check if an item exist in a list we use in membership operator.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
# for example:
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True