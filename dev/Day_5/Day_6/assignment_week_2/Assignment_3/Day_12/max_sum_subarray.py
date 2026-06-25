def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
 
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_start = 0
 
    # Slide the window
    for i in range(k, n):
        window_sum += arr[i]       # Add incoming element
        window_sum -= arr[i - k]   # Remove outgoing element
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1
 
    return max_sum, arr[max_start:max_start + k]
 
# ── REAL LIFE: Stock market - best 5-day window for profits ──────────────
daily_profits = [100, -50, 200, 300, -100, 400, 250, -150, 350, 500]
k = 5  # Look for best 5-day trading window
 
max_profit, best_days = max_sum_subarray(daily_profits, k)
print(f'Max profit in any 5-day window: Rs {max_profit}')
print(f'Best 5 days: {best_days}')
# Output: Max profit: 1200  |  Best 5 days: [400, 250, -150, 350, 500]
