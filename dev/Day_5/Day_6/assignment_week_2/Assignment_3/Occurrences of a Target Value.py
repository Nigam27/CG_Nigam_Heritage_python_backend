arr = [1, 2, 3, 2, 4, 2, 5]
target = 2

indices = []

for i in range(len(arr)):
    if arr[i] == target:
        indices.append(i)

print(indices)