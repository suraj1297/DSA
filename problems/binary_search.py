"""
There is an unsorted list of array in which after some pint only infinite integers
are present. We have to find the index of first infinite integer.

The idea here is to use the modified binary search algorithm because in binary search algorithm
we can drop half of list elements and can move in left or right direction. 
In this we can find the middle element and then we check if the middle element is infinite value
or not and then we can move the lower bound to middle  and once we find the infinite value as middle
then we can move the upper bound to middle untill we find the first index

"""

def findInfinite(arr):

    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low + high)//2
        if low == high and arr[low] == "infinite":
            return high
        if arr[mid] != "infinite":
            low = mid + 1
        elif arr[mid] == "infinite":
            high = mid
    
    return -1

print(findInfinite([1,4,2,9,8,3,6,7,"infinite","infinite","infinite","infinite","infinite","infinite"]))


"""
Now the last index we dont know and it lies at infinite.
Here we will jump index exponentially so that we can find the infinite value faster.

"""


def findInfinite2(arr):

    start = 0
    end = 1

    count = 0

    while(count < 999999999999999999999):
        count+=1

        if arr[end] == "infinite":
            break
        else:
            temp = end
            end = start * 2
            start = temp

    
    while start<=end:

        mid = start + (end-start)//2

        if start == end and arr[start] == "infinite":
            return start

        if arr[mid] != "infinite":
            start = mid + 1
        else:
            end = mid

    return -1

print(findInfinite2([1,4,2,9,8,3,6,7,9,10,11,"infinite","infinite","infinite","infinite","infinite","infinite"]))

"""
Finding pair of numbers whose sum is equal to given number.

Approach 1: Binary Approach

Approach 2: Greedy Approach 

"""

"""Binary Approach"""

def binary_approach(arr, total):
    # T(n) = O(nlogn)
    for i, a in enumerate(arr): # n

        # finding b using binary approach. log(n)
        b = total - a
        low = 0
        high = len(arr) - 1
        while(low <= high):
            mid = low + (high - low) //2

            if arr[mid] == b:
                return [i,mid]
            elif arr[mid] > b:
                high = mid - 1
            else:
                low = mid + 1
    return -1

print(binary_approach([20,40,60,80,90,120,240], 210))

""" Greedy Approach or Two Pointer Approach"""

def greedy_approach(arr, total):
    # T(n) = O(n)
    i = 0
    j = len(arr) - 1
    while(i<=j):

        if (arr[i] + arr[j]) > total:
            j -+ 1
        elif (arr[i] + arr[j]) < total:
            i += 1
        else:
            return [i,j]

    return -1

print(binary_approach([20,40,60,80,90,120,240], 210))
