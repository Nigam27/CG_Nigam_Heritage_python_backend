#Q7. Write a recursive function to find the maximum element in a list.

def find_max(arr, n):    
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    
    return max

arr = [12, 45, 7, 89, 23]

print("Maximum Element:", find_max(arr, len(arr)))