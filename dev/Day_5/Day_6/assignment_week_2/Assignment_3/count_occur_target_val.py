arr = [2, 4, 2, 6, 2, 8]
target = 2

count = 0

for num in arr:
    if num == target:
        count += 1

print("Occurrences =", count)