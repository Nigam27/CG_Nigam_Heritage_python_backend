#Q2. Modify Bubble Sort to stop early if the array becomes sorted.
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    print(f"Pass {i + 1}: {arr}")

    if not swapped:
        print("Array already sorted.")
        break

print("Sorted Array:", arr)