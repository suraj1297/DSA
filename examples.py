""""
Sum of array using D&C
"""

def sumOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sumOfArray(arr[1:])

print(sumOfArray([1,2,3,4,5]))

"""
Number of items in array using D&C
"""


def numberOfItems(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + numberOfItems(arr[1:])

print(numberOfItems([1,2,3,4,5]))

"""
Maximum number in a list using D&C
"""

def max(arr, i):
    if len(arr) == 2:
        return  arr[0] if arr[0] > arr[1] else arr[1]
    else:
        return arr[i] if arr[i] > max(arr[i+1:], i+1) else max(arr[i+1:], i+1)

print(max([1,2,3,44,5], 0))


"""
Binary Search using recursion
"""

def binary_search(arr, low, high, element):
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > high:
            return binary_search(arr, low, mid-1, element)
        else:
            return binary_search(arr, mid+1, high, element)


            
print(binary_search([1,2,3,4,5], 0, 4, 4))