students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]

topper = students[0]

for student in students:
    if student[1] > topper[1]:
        topper = student

print("Topper =", topper)