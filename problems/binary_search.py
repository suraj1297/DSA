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

