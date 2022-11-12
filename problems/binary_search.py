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


"""
Find the day when one should buy and sell shares for max profit.
In the array the index represents the day and the value price of share
on that day. First one should buy and then sell.

"""

def maxProfit(prices):

    # T(n) = O(n)
    min_price = float("inf")
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit

print(maxProfit([7,1,3,4,2,6,5]))


"""
Finding an number in 2d array using binary search

row = mid // number of columns
column = mid % number of columns

"""

def find_number(arr, target):

    low = 0
    high = ( len(arr) * len(arr[0]) ) - 1
    cols = len(arr[0])

    while(low <= high):
        mid = low + (high - low)//2

        if arr[mid//cols][mid%cols] == target:
            return [mid//cols, mid%cols]
        elif arr[mid//cols][mid%cols] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(find_number([ [1,2,3,4], [5,6,7,8], [9, 10, 11, 12] ], 8))