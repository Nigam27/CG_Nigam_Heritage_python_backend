#(b) Two Pointer (Sorted Array)
arr = [2, 7, 11, 15]
target = 9
left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print(left, right)
        break
    elif total < target:
        left += 1
    else:
        right -= 1