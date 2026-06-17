tags = {'python', 'coding', 'tutorial'}
# add() — add single element
tags.add('beginner')
print(tags) # {'python', 'coding', 'tutorial', 'beginner'}
# Adding duplicate — ignored silently
tags.add('python') # no error, no change
# update() — add multiple elements
tags.update(['advanced', 'oop'])
# remove() — removes element; raises KeyError if not found
tags.remove('beginner')
# discard() — removes element; NO error if not found ✅
tags.discard('nonexistent') # safe
# pop() — removes and returns ARBITRARY element (sets are unordered)
item = tags.pop()
print(f'Removed: {item}')
# clear() — remove everything
# tags.clear()
