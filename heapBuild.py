def buidlHeap(arr):
    
    startIndex = (len(arr)//2) - 1

    for i in range(startIndex, -1 , -1):
        heapify(arr, i)

def heapify(arr, i):
    smallest = arr[i]
    swap = None
    lc = 2*i + 1
    rc = 2*i + 2

    if lc < len(arr) and rc < len(arr):
        if arr[lc] < smallest:
            smallest = arr[lc]
            swap = "lc"
        if arr[rc] < smallest:
            smallest = arr[rc]
            swap = "rc"

        if swap == "lc":
            arr[lc] = arr[i]
            arr[i] = smallest
            print(arr[i], arr[lc], arr[rc])
            heapify(arr, lc)
        elif swap == "rc":
            arr[rc] = arr[i]
            arr[i] = smallest
            print(arr[i], arr[lc], arr[rc])
            heapify(arr, rc)

        


buidlHeap([145,40,25,65,12,48,18,20,30,35,60,70,75])