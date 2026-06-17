# Empty set — MUST use set(), not {} (that makes a dict!)
empty = set()
# Set of unique visitors
visitors = {'Alice', 'Bob', 'Carol', 'Alice', 'Bob'}
print(visitors) # {'Alice', 'Bob', 'Carol'} — duplicates removed!
# Set from list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = set(numbers)
print(unique) # {1, 2, 3, 4, 5}
# Set from string (unique characters)
chars = set('banana')
print(chars) # {'a', 'b', 'n'} — order varies
print(type(visitors)) # <class 'set'>
print(len(visitors)) # 3


tags = {'python', 'coding', 'tutorial'}
# add() — add single element
tags.add('beginner')
print(tags) # {'python', 'coding', 'tutorial', 'beginner'}