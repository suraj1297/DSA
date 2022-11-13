def bubble_sort(arr):

    # T(n) = O(n^2)

    swap = True
    count = 0
   
    for i in range(len(arr)):
        local_swap = False
        if not swap:
            return arr
        for j in range(len(arr) -i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                local_swap = True
        swap = local_swap
        count+=1

print(bubble_sort([9,3,2,6,2])) 


"""
Bubble Sort:

In swap 1 or loop 1 of i:
    9 will be compared with 3 and 9 will come at 1 and 3 at 0 -> [3,9,2,6,2]
    Then 9 will be compared with 2 and 9 will come at index 2 and 2 will come at index 1 -> [3,2,9,6,2]
    Then 9 will be compared with 6 and positions will be swaped -> [3,2,6,9,2]
    Then 9 will be compared with 2 and positions will be swaped -> [3,2,6,2,9]

    At the end of each pass the largest number will go at end by exchaging with smallest number.

    In next pass we can skip last indices as they have highest values

    ARRAY at end of pass 1: [3, 2, 6, 2, 9]


In swap 2:
    3 and 2 will be swaped -> [2,3,6,2,9]
    6 and 2 will be swaped -> [2,3,2,6,9]

In swap 3:
    3 and 2 -> [2,2,3,6,9]

In swap 4:
    Sorted array will be returned

"""

