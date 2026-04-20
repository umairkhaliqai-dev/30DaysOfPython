# 1. Declare empty list:
lst = []
print(lst)
print()
# 2. Declare 5 items in list;
emotions = ['love','hate','happy','sad','angry','surprised']
print(emotions)
print()
# 3 len of list:
print(f"len of emotional lst: {len(emotions)}")
print()
# 4 1st, middle and last item of list:
first_emotion = emotions[0]
middle_emotion = emotions[len(emotions)//2]
last_emotion = emotions[-1]
print(first_emotion,  middle_emotion,  last_emotion)
print()
# modify an emotion:
emotions[4] = 'feared'
print(emotions)
print()
#Add an emotion:
emotions.append('crazy')
print(emotions)
print()
# insert in middle:
middle_index = len(emotions)//2
emotions.insert(middle_index, 'excited')
print(emotions)
print()
result = '#; '.join(emotions)
print(result)
print(emotions.sort())
emotions.reverse()
print(emotions)
print()
print()
print()
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
print()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(redux_index)
print(full_stack)