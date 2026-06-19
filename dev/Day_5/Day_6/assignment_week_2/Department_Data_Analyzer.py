employees = [
    ("Rahul", "HR"),
    ("Priya", "IT"),
    ("Amit", "HR"),
    ("Sneha", "Finance"),
    ("Rohan", "IT")
]

dept_count = {}

for name, dept in employees:
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1

print("Department-wise Employee Count:")
for dept, count in dept_count.items():
    print(dept, ":", count)