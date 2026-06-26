def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
 
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)    # Sort left of pivot
        quick_sort(arr, pivot_idx + 1, high)   # Sort right of pivot
    return arr
 
def partition(arr, low, high):
    pivot = arr[high]   # Last element as pivot
    i = low - 1         # Boundary of 'less than' region
 
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # Swap into 'less than' region
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot
    return i + 1                                     # Return pivot's final index
 
# ── REAL LIFE: Sort food delivery orders by estimated time ───────────────
delivery_minutes = [45, 12, 30, 8, 52, 25, 18, 40]
quick_sort(delivery_minutes)
print('Orders by delivery time (minutes):', delivery_minutes)
# Output: [8, 12, 18, 25, 30, 40, 45, 52]
print('Next delivery:', delivery_minutes[0], 'minutes')  # Next delivery: 8 min
