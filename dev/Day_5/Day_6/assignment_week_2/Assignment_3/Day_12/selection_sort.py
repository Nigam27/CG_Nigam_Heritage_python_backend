def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i                          # Assume current position is minimum
 
        for j in range(i + 1, n):           # Find actual minimum in unsorted portion
            if arr[j] < arr[min_idx]:
                min_idx = j
 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap minimum to front
 
    return arr
 
# ── REAL LIFE: Select cheapest items to fill a gift box ─────────────────
item_prices = [299, 150, 499, 75, 350, 225, 125]
sorted_prices = selection_sort(item_prices.copy())
print('Prices low to high:', sorted_prices)
# Top 3 cheapest items for gift box:
print('3 cheapest items:', sorted_prices[:3])  # [75, 125, 150]
