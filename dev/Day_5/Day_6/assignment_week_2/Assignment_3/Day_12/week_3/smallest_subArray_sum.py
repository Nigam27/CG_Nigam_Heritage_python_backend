#Q9.Find the smallest subarray with sum greater than or equal to a target using Sliding Window.
arr = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
min_length = float('inf')

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= arr[left]
        left += 1

if min_length == float('inf'):
    print(0)
else:
    print("Minimum Length:", min_length)