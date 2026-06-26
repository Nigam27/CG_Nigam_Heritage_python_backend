#Q6. Count comparisons and shifts in Insertion Sort.
arr = [12, 11, 13, 5, 6]

comparisons = 0
shifts = 0

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0:
        comparisons += 1

        if arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        else:
            break

    arr[j + 1] = key

print("Sorted Array:", arr)
print("Comparisons:", comparisons)
print("Shifts:", shifts)