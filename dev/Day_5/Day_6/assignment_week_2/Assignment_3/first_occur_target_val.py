arr = [5, 7, 9, 7, 10]
target = 7

for i in range(len(arr)):
    if arr[i] == target:
        print("First occurrence at index", i)
        break