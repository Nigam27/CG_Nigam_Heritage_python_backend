arr = [12, 45, 7, 89, 23]

max_value = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]

print("Maximum element =", max_value)