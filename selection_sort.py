"""
Selction sort:

Time complexity = O(n^2)

"""

def selection_sort(arr):
    
    for i in range(len(arr)):
        smallest = arr[i]
        for index, el in enumerate(arr[i+1:]):
            if smallest > el:
                arr[i+index+1] = smallest
                smallest = el
                arr[i] = el

    return arr

print(selection_sort([5,2,8,1,9,2,4]))
