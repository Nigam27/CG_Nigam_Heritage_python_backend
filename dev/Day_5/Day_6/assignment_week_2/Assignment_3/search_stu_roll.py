students = [
    [101, "Alice"],
    [102, "Bob"],
    [103, "Charlie"]
]

roll = 102

for student in students:
    if student[0] == roll:
        print("Student Found:", student)
        break
else:
    print("Student not found")