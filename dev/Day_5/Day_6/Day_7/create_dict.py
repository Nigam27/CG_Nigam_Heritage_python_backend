# Empty dictionary
empty = {}
# Student profile
student = {
 'name': 'Alice',
 'age': 21,
 'gpa': 8.7,
 'courses': ['Math', 'Physics', 'CS']
}
# Product inventory
inventory = {
 'apple': {'price': 40, 'stock': 100},
 'banana': {'price': 20, 'stock': 200},
 'mango': {'price': 80, 'stock': 50}
}
# Using dict() constructor
config = dict(host='localhost', port=5432, db='mydb')
# Dict from two lists using zip()
keys = ['name', 'city', 'country']
values = ['Alice', 'Delhi', 'India']
profile = dict(zip(keys, values))
print(profile) # {'name': 'Alice', 'city': 'Delhi', 'country': 'India'}