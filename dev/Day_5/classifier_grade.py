# Grade Classifier — Real-World Example

def classify_grade(marks_list):
    if not marks_list or len(marks_list) == 0:
        return 'No marks provided'

    # Validate all marks are in range
    for mark in marks_list:
        if not (0 <= mark <= 100):
            return f'Invalid mark: {mark}. Must be 0-100'

    average = sum(marks_list) / len(marks_list)
    subjects_failed = sum(1 for m in marks_list if m < 35)

    # Check for fail first
    if subjects_failed > 0:
        grade = 'F'
        remark = f'Failed in {subjects_failed} subject(s). Re-appear required.'
    elif average >= 90:
        grade = 'A+'
        remark = 'Outstanding performance!'
    elif average >= 80:
        grade = 'A'
        remark = 'Excellent work!'
    elif average >= 70:
        grade = 'B'
        remark = 'Good performance. Keep it up!'
    elif average >= 60:
        grade = 'C'
        remark = 'Average performance. Work harder.'
    elif average >= 50:
        grade = 'D'
        remark = 'Below average. Needs improvement.'
    else:
        grade = 'E'
        remark = 'Very low marks. Seek extra coaching.'

    return {
        'marks': marks_list,
        'average': round(average, 2),
        'grade': grade,
        'remark': remark
    }

# Test the classifier
student_marks = [88, 92, 75, 90, 85]

result = classify_grade(student_marks)

print("=== REPORT CARD ===")
print(f"Marks   : {result['marks']}")
print(f"Average : {result['average']}")
print(f"Grade   : {result['grade']}")
print(f"Remark  : {result['remark']}")