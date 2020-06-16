# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = True
    while swaps:
        swaps = 0
        for index, item in enumerate(arr):
            if index + 1 < len(arr):
                if arr[index + 1] < item:
                    arr[index], arr[index + 1] = arr[index + 1], arr[index]
                    swaps += 1


    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(array, maximum=None):
    if array:
        if not maximum:
            maximum = max(array) + 1
        size = len(array)
        output = [0] * size

        # Initialize count array
        count = [0] * maximum

        # Store the count of each elements in count array
        for i in range(0, size):
            if array[i] < 0:
                return "Error, negative numbers not allowed in Count Sort"
            count[array[i]] += 1

        # Store the cummulative count
        for i in range(1, maximum):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = size - 1
        while i >= 0:
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            array[i] = abs(output[i])



    return array
