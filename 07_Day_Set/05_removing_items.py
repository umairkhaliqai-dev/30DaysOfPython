# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
#The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(st)
print(fruits)
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
print(fruits)
