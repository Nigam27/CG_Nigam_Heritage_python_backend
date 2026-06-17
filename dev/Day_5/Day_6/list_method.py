employees = ['Alice', 'Bob', 'Carol']
# New employee joins
employees.append('David')
employees.append('Eva')
print(employees)
# ['Alice', 'Bob', 'Carol', 'David', 'Eva']
# append() adds ONE item at a time
# To add multiple items, use extend()
employees.extend(['Frank', 'Grace'])
print(employees)
# ['Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Grace']


# insert() — Add at Specific Position
tasks = ['Write report', 'Send email', 'Attend meeting']
# Urgent task needs to be first
tasks.insert(0, 'Fix critical bug') # insert at index 0
print(tasks)
# ['Fix critical bug', 'Write report', 'Send email', 'Attend meeting']
# Insert in the middle
tasks.insert(2, 'Code review') # at index 2
print(tasks)
# ['Fix critical bug', 'Write report', 'Code review', 'Send email', 'Attend meeting']

# — remove() — Remove by Value

order = ['pizza', 'burger', 'fries', 'coke', 'burger']
# Customer cancels one burger (removes FIRST occurrence)
order.remove('burger')
print(order) # ['pizza', 'fries', 'coke', 'burger']
# Error if item not found:
# order.remove('pasta') → ValueError: list.remove(x): x not in list
# Safe way to remove
if 'pasta' in order:
 order.remove('pasta')
else:
 print('Item not in order')
 
 #— pop() — Remove by Index
 
 queue = ['Task1', 'Task2', 'Task3', 'Task4']
# Remove last item (stack behavior)
last = queue.pop()
print(last) # Task4
print(queue) # ['Task1', 'Task2', 'Task3']
# Remove specific index
first = queue.pop(0) # FIFO behavior
print(first) # Task1
print(queue) # ['Task2', 'Task3']

