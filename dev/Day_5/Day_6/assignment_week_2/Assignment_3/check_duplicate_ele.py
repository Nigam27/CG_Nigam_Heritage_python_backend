def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]   # return the duplicate element
    return None                # no duplicate found

arr = [10, 20, 30, 40, 20]

duplicate = find_duplicate(arr)

if duplicate is not None:
    print("Duplicate element:", duplicate)
else:
    print("No duplicate element found")