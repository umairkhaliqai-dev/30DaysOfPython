# Once a set is created we cannot change any items and we can also add additional items.
# Add one item using add()
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
# for example: 
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
# we can add multip[le items by using update operator
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)
