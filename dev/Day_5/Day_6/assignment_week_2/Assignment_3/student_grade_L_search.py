students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 68]
]

name = "Charlie"

for student in students:
    if student[0] == name:
        marks = student[1]

        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        print("Name =", name)
        print("Marks =", marks)
        print("Grade =", grade)
        break
else:
    print("Student not found")