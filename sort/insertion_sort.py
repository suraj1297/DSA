def insertionSort(arr):

    for i in range(1, len(arr)-1):
        for j in range(i, 0, -1): 
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break
    return arr


print(insertionSort([20,11,4,22,5,8,2,55]))