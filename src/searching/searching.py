# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    for index in range(0, len(arr)):
        if arr[index] == target:
            return index

    return -1  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    # TO-DO: add missing code
    while high >= low:
        midpoint = (low + high) // 2
        if arr[midpoint] == target:
            return midpoint
        elif target < arr[midpoint]:
            high = midpoint
        else:
            low = midpoint

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

