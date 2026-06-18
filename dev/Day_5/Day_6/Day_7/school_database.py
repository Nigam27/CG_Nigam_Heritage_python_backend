school = {
 'CS101': {
 'teacher': 'Dr. Smith',
 'students': ['Alice', 'Bob'],
 'credits': 4
 },
 'MA201': {
 'teacher': 'Prof. Patel',
 'students': ['Carol', 'David', 'Eve'],
 'credits': 3
 }
}
# Access nested values
print(school['CS101']['teacher']) # Dr. Smith
print(school['MA201']['students'][0]) # Carol
# Add a student to CS101
school['CS101']['students'].append('Frank')
# Iterate nested dict
for course, info in school.items():
 print(f'{course}: {info["teacher"]} — {len(info["students"])} students')