import math

def heapify(arr):

    index = math.ceil(len(arr) // 2 ) - 1

    for i in range(index+1, -1, -1):
        check(arr, i)

    return arr


def check(arr, i):

    root = arr[i]
    li = 2 * i + 1
    ri = 2 * i + 2
    

    if li >= len(arr):
        lc = math.inf
    else:
        lc = arr[li]

    if ri >= len(arr):
        rc = math.inf
    else:
        rc = arr[ri]

    if lc < root and lc < rc:
        temp = arr[li]
        arr[li] = root
        arr[i] = temp
        check(arr, li)
    elif rc < root and rc < lc:
        temp = arr[ri]
        arr[ri] = root
        arr[i] = temp
        check(arr, ri)



# print(heapify([145,40,25,65,12,48,18,20,30,35,60,70,75, 11]))

if __name__ == "__main__":
    print(heapify([145,40,25,65,12,48,18,20,30,35,60,70,75, 11]))
