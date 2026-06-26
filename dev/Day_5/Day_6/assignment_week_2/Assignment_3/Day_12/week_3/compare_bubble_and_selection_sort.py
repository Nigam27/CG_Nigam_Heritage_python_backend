#Q4. Compare Bubble Sort and Selection Sort using random datasets.
import random
import time

arr1 = random.sample(range(1, 101), 20)
arr2 = arr1.copy()

# Bubble Sort
start = time.time()

for i in range(len(arr1) - 1):
    for j in range(len(arr1) - 1 - i):
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

bubble_time = time.time() - start

# Selection Sort
start = time.time()

for i in range(len(arr2)):
    min_index = i

    for j in range(i + 1, len(arr2)):
        if arr2[j] < arr2[min_index]:
            min_index = j

    arr2[i], arr2[min_index] = arr2[min_index], arr2[i]

selection_time = time.time() - start

print("Bubble Sort Time:", bubble_time)
print("Selection Sort Time:", selection_time)