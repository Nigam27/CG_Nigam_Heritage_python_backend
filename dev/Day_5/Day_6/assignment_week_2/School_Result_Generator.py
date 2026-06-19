marks = {
    "Math": int(input("Enter marks in Math: ")),
    "Science": int(input("Enter marks in Science: ")),
    "English": int(input("Enter marks in English: ")),
    "Hindi": int(input("Enter marks in Hindi: ")),
    "Social Science": int(input("Enter marks in Social Science: "))    
}

total = sum(marks.values())
percentage = total / len(marks)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\nMarks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)