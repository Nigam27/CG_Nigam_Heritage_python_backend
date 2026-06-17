# SCENARIO 1: Online Shopping Cart (items can repeat)
cart = ['iPhone', 'AirPods', 'iPhone', 'Case'] # LIST
# SCENARIO 2: GPS Pin (fixed coordinates)
office_location = (28.6139, 77.2090) # TUPLE
# SCENARIO 3: User profile (lookup by field name)
user = {'id': 101, 'name': 'Alice', 'role': 'admin'} # DICT
# SCENARIO 4: Track unique page visits
visited_pages = {'/home', '/about', '/contact'} # SET
# SCENARIO 5: Word frequency count
text = 'the cat sat on the mat the cat'
freq = {}
for word in text.split():
 freq[word] = freq.get(word, 0) + 1 # DICT
print(freq) # {'the': 3, 'cat': 2, 'sat': 1, ...}
# SCENARIO 6: Find common students in two classes
class_A = {'Alice', 'Bob', 'Carol', 'David'}
class_B = {'Carol', 'David', 'Eve', 'Frank'}
common = class_A & class_B # SET intersection
print(common) # {'Carol', 'David'}
# SCENARIO 7: Remove duplicates while preserving order
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_ordered = list(dict.fromkeys(data)) # DICT trick
print(unique_ordered) # [3, 1, 4, 5, 9, 2, 6]
