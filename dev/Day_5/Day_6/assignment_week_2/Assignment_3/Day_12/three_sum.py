def three_sum(arr):
    arr.sort()                          # Sort first!
    result = []
 
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue                     # Skip duplicates
 
        left, right = i + 1, len(arr) - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result
 
# Example
nums = [-4, -1, -1, 0, 1, 2]
print(three_sum(nums))  # [[-1, -1, 2], [-1, 0, 1]]
