# Empty tuple
empty = ()
# Single element tuple — MUST have trailing comma!
single = (42,) # ✅ This is a tuple
not_tuple = (42) # ❌ This is just int 42 in parentheses
# GPS coordinates
delhi_coords = (28.6139, 77.2090)
mumbai_coords = (19.0760, 72.8777)
# Student record
student = ('Alice', 20, 'B.Tech', 8.7)
# Tuple without parentheses (packing)
rgb_red = 255, 0, 0 # Python auto-packs as tuple
# From list
t = tuple([1, 2, 3]) # (1, 2, 3)
print(type(delhi_coords)) # <class 'tuple'>
print(len(student)) # 4

#Accessing Tuple Elements

record = ('EMP001', 'Alice', 'Engineering', 75000, 'Mumbai')
# 0 1 2 3 4
print(record[0]) # EMP001
print(record[1]) # Alice
print(record[-1]) # Mumbai
print(record[1:3]) # ('Alice', 'Engineering')
# Tuples are IMMUTABLE — this will ERROR:
# record[0] = 'EMP002' → TypeError: 'tuple' object does not support item