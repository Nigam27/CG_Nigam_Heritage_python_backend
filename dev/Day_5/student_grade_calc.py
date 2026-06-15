name = input("Student Name : ")
marks_s = int(input("Science Marks: "))
marks_m = int(input("Maths Marks : "))
marks_e = int(input("English Marks: "))
total = marks_s + marks_m + marks_e
average = total / 3
if average >= 90:
 grade = "A+"
elif average >= 75:
 grade = "A"
elif average >= 60:
 grade = "B"
else:
 grade = "C"
print(f"{name} | Total: {total} | Avg: {average:.1f} | Grade: {grade}")

