def quickSort(arr):
    if len(arr)<2:   # base case: if array has only 1 element then return it
        return arr
    
    pivot = arr[0] # chooses the first element as a pivot
    less = [x for x in arr[1:] if x<=pivot]#everything less than the pivot
    more = [x for x in arr[1:] if x>pivot]#everything more than the pivot

    return quickSort(less) + [pivot] + quickSort(more)#in the return statement concantenate the arrays after recursively calling the function on each side untill there is only one element left in each
    

massive_unsorted_list = [
    541, 753, 221, 984, 385, 173, 610, 891, 409, 726,
    204, 337, 118, 662, 882, 994, 556, 229, 347, 901,
    123, 654, 987, 775, 432, 569, 309, 876, 287, 459,
    633, 171, 823, 941, 682, 245, 507, 869, 112, 788,
    357, 613, 224, 995, 468, 928, 103, 789, 565, 202,
    441, 706, 333, 798, 212, 982, 854, 128, 496, 680,
    317, 729, 439, 897, 621, 174, 907, 540, 639, 478,
    123, 957, 304, 830, 265, 798, 356, 511, 919, 227,
    863, 472, 211, 932, 574, 308, 720, 543, 890, 225,
    361, 981, 574, 118, 622, 327, 891, 178, 439, 675,
    
]
print(quickSort(massive_unsorted_list))