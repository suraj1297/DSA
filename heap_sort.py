import heap, math

arr = [145,40,25,65,12,48,18,20,30,35,60,70,75]

heapified = heap.heapify(arr)

def heap_sort(arr):

    sorted = []
    for i in range(len(arr)):
        sorted.append(arr.pop(0))
        if len(arr) > 1:
            arr.insert(0, arr.pop())
            heap.check(arr, 0)

    return sorted


if __name__ == "__main__":
    print(heap_sort(heapified))