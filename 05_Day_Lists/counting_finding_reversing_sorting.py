#  Counting Items in a List
# Using count() to find how many times an item appears.
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
count = fruits.count('apple')
print(count)  #3
print()
# Finding Index of an Item
# Using index() to find the first occurrence's position.
fruits = ['apple', 'banana', 'orange', 'banana']
position = fruits.index('banana')
print(position)  #1
print()
# Reversing a List
# Using reverse() to reverse the order of items.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # goes in reverse order from 5 to 1
print()
# Sorting List Items
# Using sort() for ascending order or sort(reverse=True) for descending.
# Ascending order
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Descending order
numbers.sort(reverse=True)
print(numbers)  

# Sorting strings
fruits = ['banana', 'apple', 'mango', 'orange']
fruits.sort()
print(fruits)  # by numerically alphabet setting like A, B, C etc... 

print()
print("+=" *50)
# Key Takeaways for Day 5 :-
# Topic	       Key Method/Concept
# Creation	   [] brackets
# Access	   list[index]
# Slice	       [start:end]
# Add	       append(), insert()
# Remove	   remove(), pop(), del
# Clear	       clear()
# Copy	       copy()
# Join	       + or extend()
# Count	       count()
# Index	       index()
# Reverse	   reverse()
# Sort	       sort()
