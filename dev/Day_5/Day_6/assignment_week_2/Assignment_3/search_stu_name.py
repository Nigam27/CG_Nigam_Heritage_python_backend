students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]

name = "Bob"

for student in students:
    if student[0] == name:
        print("Found:", student)
        break
else:
    print("Not found")