def longest_subarray_sum_k(arr, k):
    left = 0
    window_sum = 0
    max_length = 0
    best_start = 0
 
    for right in range(len(arr)):
        window_sum += arr[right]         # Expand window
 
        while window_sum > k:            # Shrink if over budget
            window_sum -= arr[left]
            left += 1
 
        if right - left + 1 > max_length:
            max_length = right - left + 1
            best_start = left
 
    return max_length, arr[best_start:best_start + max_length]
 
# ── REAL LIFE: Budget travel — max days within budget of Rs 5000 ──────────
daily_costs = [800, 1200, 500, 2000, 600, 400, 1500, 300, 900, 700]
budget = 5000
 
days, trip = longest_subarray_sum_k(daily_costs, budget)
print(f'Max consecutive travel days within budget: {days}')
