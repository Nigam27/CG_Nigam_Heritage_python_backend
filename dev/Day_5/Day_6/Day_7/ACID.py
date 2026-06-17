student = {'name': 'Bob', 'age': 20, 'gpa': 7.8}
# Access by key
print(student['name']) # Bob
# Add new key-value pair
student['email'] = 'bob@example.com'
# Update existing value
student['gpa'] = 8.2
# Delete a key
del student['age']
# Check key existence
if 'email' in student:
 print('Has email')
print(student)
# {'name': 'Bob', 'gpa': 8.2, 'email': 'bob@example.com'}
