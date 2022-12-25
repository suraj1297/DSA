def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = len(arr) // 2
        left = [x for x in arr if x < arr[pivot]]
        right = [x for x in arr if x > arr[pivot]]

        return quick_sort(left) + [arr[pivot]] + quick_sort(right)



print(quick_sort([31, 20, 33, 4 , 2, 1]))
