arr = [12, 45, 7, 89, 23]

min_value = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min_value:
        min_value = arr[i]

print("Minimum element =", min_value)