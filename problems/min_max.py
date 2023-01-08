def minmax(arr):
    print(arr)
    if len(arr) == 1:
        return [arr[0], arr[1]]
    elif len(arr) == 2:
        min_ = arr[0] if arr[0] < arr[1] else arr[1]
        max_ = arr[1] if min_ == arr[0] else arr[0]
        return [min_, max_]
    else:
        mid = len(arr) // 2
        
        min1, max1 = minmax(arr[0: mid]) 
        min2, max2 = minmax(arr[mid: ])

        print(min1, max1)
        print(min2, max2)

        min = min1 if min1 < min2 else min2
        max = max1 if max1 > max2 else max2

    return [min, max]

print(minmax([55, 66,77,88,4, 1,2,55]))

