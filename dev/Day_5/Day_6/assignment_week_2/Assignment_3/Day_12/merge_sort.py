def merge_sort(arr):
    # BASE CASE: Single element is already sorted
    if len(arr) <= 1:
        return arr
 
    # DIVIDE: Split into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])    # Recursively sort left
    right_half = merge_sort(arr[mid:])   # Recursively sort right
 
    # CONQUER: Merge sorted halves
    return merge(left_half, right_half)
 
def merge(left, right):
    result = []
    i = j = 0
 
    # Compare elements from both halves and add smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
 
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 
# ── REAL LIFE: Merge two sorted customer lists from two branches ──────────
branch_A_customers = [1005, 1023, 1047, 1089]   # already sorted by ID
branch_B_customers = [1012, 1034, 1056, 1090]   # already sorted by ID
 
combined = merge(branch_A_customers, branch_B_customers)
print('Merged customer list:', combined)
# Output: [1005, 1012, 1023, 1034, 1047, 1056, 1089, 1090]
