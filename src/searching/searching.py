def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid


    return -1  # not found
