"""
Student Grade Calculator
Calculates average marks and assigns letter grades
"""
 
# Display program header
print("=" * 45)
print("     STUDENT GRADE CALCULATOR")
print("=" * 45)
 
# Collect student information
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
 
# Collect marks for 5 subjects
print("\nEnter marks out of 100 for each subject:")
maths = float(input("  Mathematics: "))
science = float(input("  Science: "))
english = float(input("  English: "))
history = float(input("  History: "))
computer = float(input("  Computer Science: "))
 
# Calculate total and average
total = maths + science + english + history + computer
average = total / 5
 
# Assign letter grade based on average
if average >= 90:
    grade = "A+"
    remark = "Outstanding"
elif average >= 80:
    grade = "A"
    remark = "Excellent"
elif average >= 70:
    grade = "B"
    remark = "Good"
elif average >= 60:
    grade = "C"
    remark = "Satisfactory"
elif average >= 40:
    grade = "D"
    remark = "Needs Improvement"
else:
    grade = "F"
    remark = "Fail"
 
# Display result card
print("\n" + "=" * 45)
print("           RESULT CARD")
print("=" * 45)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("-" * 45)
print(f"Mathematics  : {maths}")
print(f"Science      : {science}")
print(f"English      : {english}")
print(f"History      : {history}")
print(f"Computer Sc. : {computer}")
print("-" * 45)
