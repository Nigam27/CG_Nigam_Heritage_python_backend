# ─── Data Setup ───────────────────────────────

students = []  # LIST: ordered student records

def add_student(roll, name, branch, marks):
    record = (roll, name, branch, marks)  # TUPLE: immutable record
    students.append(record)

add_student('CS001', 'Alice', 'CS', [85, 90, 78, 92, 88])
add_student('CS002', 'Bob', 'CS', [70, 65, 80, 75, 72])
add_student('EC001', 'Carol', 'ECE', [90, 92, 88, 95, 91])
add_student('ME001', 'David', 'Mech', [60, 55, 70, 65, 58])

# ─── Build Grade Dictionary ────────────────────

grade_book = {}  # DICT: roll → grade info

for roll, name, branch, marks in students:  # TUPLE unpacking
    avg = sum(marks) / len(marks)
    grade = 'A' if avg >= 85 else 'B' if avg >= 70 else 'C'

    grade_book[roll] = {
        'name': name,
        'avg': round(avg, 2),
        'grade': grade
    }

# ─── Set Operations on Branches ────────────────

cs_students = {r for r, n, b, m in students if b == 'CS'}   # SET comprehension
ece_students = {r for r, n, b, m in students if b == 'ECE'}

# ─── Display Results ────────────────────────────

print("=== GRADE REPORT ===")

for roll, info in grade_book.items():
    print(
        f"{roll}: {info['name']:<8} "
        f"Avg: {info['avg']:6.2f} "
        f"Grade: {info['grade']}"
    )

print(f"\nCS students: {cs_students}")

print(
    "Top scorers (Grade A):",
    {r for r, i in grade_book.items() if i['grade'] == 'A'}
)