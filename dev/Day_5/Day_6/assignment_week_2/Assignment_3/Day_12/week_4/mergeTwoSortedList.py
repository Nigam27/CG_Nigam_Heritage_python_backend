def mergeTwoSortedList(arr1,arr2):
    n,m = len(arr1),len(arr2)
    result = []

    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if len(result) == 0 or result[-1]!=arr1[i]:
                result.append(arr1[i])        
            i += 1
        else:
            if len(result) == 0 or result[-1]!=arr2[j]:
                result.append(arr2[j])        
            j += 1

    while i < n:
        if len(result) == 0 or result[-1]!=arr1[i]:
                result.append(arr1[i])        
        i += 1
        
    while j < m:
        if len(result) == 0 or result[-1]!=arr2[j]:
                result.append(arr2[j])        
        j += 1
        
    return result
arr1 = [2, 5, 9]
arr2 = [1, 4, 8]
    

print(mergeTwoSortedList(arr1,arr2))