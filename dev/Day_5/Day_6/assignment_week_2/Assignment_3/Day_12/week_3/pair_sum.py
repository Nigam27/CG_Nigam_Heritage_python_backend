#Q8.Solve the Pair Sum problem using brute force and Two-Pointer and compare complexities.

arr = [2, 7, 11, 15]
target = 9
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print(i, j)