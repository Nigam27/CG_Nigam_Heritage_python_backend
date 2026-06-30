students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]

lowest = students[0]

for student in students:
    if student[1] < lowest[1]:
        lowest = student

print("Lowest scorer =", lowest)