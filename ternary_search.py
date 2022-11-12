"""
Ternary is similar to binary, just that instead 
of dividing in two parts we divide it in three 
parts by finding two mids.


"""


def ternary_search(arr, key):

    low = 0
    high = len(arr) - 1

    while low<=high:
        mid1 = low + (high - low) // 2
        mid2 = high - (high - low) // 2

        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif arr[mid1] > key:
            high = mid1 - 1
        elif arr[mid2] < key:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1

print(ternary_search([1,2,3,4,5,6,7,8,9], 7))


""" Recursive Approach """
def ternary_search2(arr, low, high, key):

    if low == high:
        if arr[low] == key:
            return high 
        return -1
    else:
        mid1 = low + (high - low)//2
        mid2 = high - (high - low)//2

        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif arr[mid1] > key:
            return ternary_search(arr, low, mid1-1, key)
        elif arr[mid2] < key:
            return ternary_search(arr, mid2+1, high ,key)
        else:
            return ternary_search(arr, mid1+1, mid2-1, key)

print(ternary_search([1,2,3,4,5,6,7,8,9], 7))