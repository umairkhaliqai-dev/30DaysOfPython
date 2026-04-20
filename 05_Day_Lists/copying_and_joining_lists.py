# Copying a List
# Using copy() to create a separate copy (not just a reference).
fruits = ['apple', 'banana', 'orange']
fruits_copy = fruits.copy()
fruits_copy.append('mango')
print(fruits)       
print(fruits_copy)  

print()
# Joining Lists
# Using + operator or extend() to combine lists.
# Method 1: Using + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  

# Method 2: Using extend()
list1.extend(list2)
print(list1)  
