# Unpack GPS coordinates
coords = (28.6139, 77.2090)
latitude, longitude = coords
print(f'Lat: {latitude}, Lon: {longitude}')
# Lat: 28.6139, Lon: 77.209
# Unpack student record
student = ('Bob', 21, 'CSE', 8.5)
name, age, branch, gpa = student
print(f'{name} is {age} years old, GPA: {gpa}')
# Unpack in a for loop (very common!)
employees = [('Alice', 50000), ('Bob', 60000), ('Carol', 55000)]
for name, salary in employees:
 print(f'{name} earns ₹{salary:,}')
# Extended unpacking with * (star)
first, *middle, last = (10, 20, 30, 40, 50)
print(first) # 10
print(middle) # [20, 30, 40]
print(last) # 50
# Ignore values with _
name, _, branch, _ = ('Alice', 20, 'CSE', 8.9)
print(name, branch) # Alice CSE

#— Swapping Variables with Tuple Unpacking

# Traditional way (other languages)
a = 10
b = 20
temp = a
a = b
b = temp
# Pythonic way using tuple unpacking ✨
a = 10
b = 20
a, b = b, a
print(a, b) # 20 10
# Real example: sort two numbers
x, y = 100, 45
if x < y:
 x, y = y, x # ensure x is always larger
print(f'Larger: {x}, Smaller: {y}') # Larger: 100, Smaller: 45
# Swap in sorting algorithms
arr = [3, 1, 4, 1, 5]
arr[0], arr[2] = arr[2], arr[0] # swap index 0 and 2
print(arr) # [4, 1, 3, 1, 5]


#Tuples as Dictionary Keys & Function Returns
# Tuple as dict key (real: storing distances between cities)
distances = {
 ('Delhi', 'Mumbai'): 1400,
 ('Delhi', 'Chennai'): 2200,
 ('Mumbai', 'Chennai'): 1330
}
print(distances[('Delhi', 'Mumbai')]) # 1400
# Function returning multiple values (as tuple)
def get_min_max(numbers):
 return min(numbers), max(numbers) # returns tuple
scores = [85, 92, 78, 95, 88]
low, high = get_min_max(scores)
print(f'Lowest: {low}, Highest: {high}') # Lowest: 78, Highest: 95
# Named tuple for clarity
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y) # 3 4
print(p[0], p[1]) # 3 4


#Looping Through Tuples
# Simple iteration
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')
for month in months:
 print(month, end=' ')
# Jan Feb Mar Apr May Jun
# With enumerate
for i, month in enumerate(months, start=1):
 print(f'{i:02d}: {month}')
# Iterating list of tuples (very common with databases)
db_records = [
 (1, 'Alice', 'HR', 55000),
 (2, 'Bob', 'IT', 70000),
 (3, 'Carol', 'Finance', 65000)
]
print(f'{'ID':<5}{'Name':<10}{'Dept':<10}{'Salary':>10}')
print('-' * 35)
for id, name, dept, salary in db_records:
 print(f'{id:<5}{name:<10}{dept:<10}{salary:>10,}')
