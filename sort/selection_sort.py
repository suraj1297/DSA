"""
Selction sort:

Time complexity = O(n^2)

"""

def selection_sort(arr):
    
    for i in range(len(arr)):
        smallest = i
        for index, el in enumerate(arr[i+1:]):
            if arr[smallest] > el:
                smallest = i+index+1
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        print(arr)
    return arr

print(selection_sort([5,2,8,1,9,2,4]))


"""
Selection Sort:

With each iteration i, it finds the index of the smallest number and then swap the
smallest number at the i'th position such that the smallest number keeps coming in
front with each iteration

I 1 -> [1, 2, 8, 5, 9, 2, 4]

I 2 -> [1, 2, 8, 5, 9, 2, 4]

I 3 -> [1, 2, 2, 5, 9, 8, 4]

I 4 -> [1, 2, 2, 4, 9, 8, 5]

I 5 -> [1, 2, 2, 4, 5, 8, 9]

I 6 -> [1, 2, 2, 4, 5, 8, 9]

I 7 -> [1, 2, 2, 4, 5, 8, 9]

"""
