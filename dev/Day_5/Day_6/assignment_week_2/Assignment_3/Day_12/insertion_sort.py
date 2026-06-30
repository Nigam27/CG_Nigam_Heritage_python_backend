def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]                    # Element to be placed
        j = i - 1
 
        # Shift elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
 
        arr[j + 1] = key               # Place key in correct position
 
    return arr
 
# ── REAL LIFE: Inserting a new employee record into sorted HR list ────────
hr_employee_ids = [1001, 1003, 1007, 1012, 1020]
new_employee = 1008
 
hr_employee_ids.append(new_employee)
sorted_ids = insertion_sort(hr_employee_ids)
print('Updated employee ID list:', sorted_ids)
# Output: [1001, 1003, 1007, 1008, 1012, 1020]
 
