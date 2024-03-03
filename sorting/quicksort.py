def quickSort(arr):
    if len(arr)<2:   # base case: if array has only 1 element then return it
        return arr
    
    pivot = arr[0] # chooses the first element as a pivot
    less = [x for x in arr[1:] if x<=pivot]#everything less than the pivot
    more = [x for x in arr[1:] if x>pivot]#everything more than the pivot

    return quickSort(less) + [pivot] + quickSort(more)#in the return statement concantenate the arrays after recursively calling the function on each side untill there is only one element left in each
    
print(quickSort([2,12,3,45,6]))