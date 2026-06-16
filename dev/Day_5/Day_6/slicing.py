scores = [55, 62, 70, 78, 85, 90, 95, 100]
# 0 1 2 3 4 5 6 7
# Basic slice
print(scores[2:5]) # [70, 78, 85] → index 2,3,4
# From beginning
print(scores[:3]) # [55, 62, 70] → first 3 items
# Till end
print(scores[5:]) # [90, 95, 100] → from index 5 onward
# Full copy
print(scores[:]) # [55, 62, 70, 78, 85, 90, 95, 100]
# Step slicing — every 2nd element
print(scores[::2]) # [55, 70, 85, 95]

# Reverse the list
print(scores[::-1]) # [100, 95, 90, 85, 78, 70, 62, 55]
# Negative slicing
print(scores[-3:]) # [95, 100] ... wait:
print(scores[-3:]) # [90, 95, 100] → last 3 items