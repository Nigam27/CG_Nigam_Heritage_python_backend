#Q3. Implement Selection Sort and count swaps.
arr = [64, 25, 12, 22, 11]
n = len(arr)

swaps = 0

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

print("Sorted Array:", arr)
print("Total Swaps:", swaps)