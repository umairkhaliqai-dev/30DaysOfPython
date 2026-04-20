#  Removing Items from a List
# Using remove() to delete the first occurrence of an item
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  #    ['apple', 'orange', 'banana']
print()
print()
# Removing Items Using Pop
# Using pop() removes the last item, or at specified index.
fruits = ['apple', 'banana', 'orange']
popped = fruits.pop()  # Removes last item
print(popped)   #  orange
print(fruits)   #  ['apple', 'banana']

# Remove at specific index
fruits.pop(0)
print(fruits)   #  ['banana']

print()
print("+" *10)
fruits_lst = ['apple', 'watermelon','melon','kiwi']
fruits_lst.pop(0)
print(fruits_lst) # returns with [watermelon to kiwi]

print()
popped_fruit = fruits_lst.pop(0)
print(popped_fruit ) # so iut depends how many times i have run pop command will decide what to return with the remaining list values. 
print()
print()
# Removing Items Using Del
# Using del keyword to delete an item by index or delete entire list.
fruits = ['apple', 'banana', 'orange', 'mango']
del fruits[2]  # Removes item at index 2
print(fruits)  #  ['apple', 'banana', 'mango']

del fruits     # Deletes the entire list
# print(fruits)  # This would cause NameError
print()
# Clearing List Items
# Using clear() to remove all items but keep the list.
fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)  
