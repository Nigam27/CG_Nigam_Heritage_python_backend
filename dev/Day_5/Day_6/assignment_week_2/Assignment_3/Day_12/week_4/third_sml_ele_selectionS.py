arr = [17, 8, 25, 4, 13, 30]

n = len(arr)

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted:", arr)
print("3rd Smallest:", arr[2])