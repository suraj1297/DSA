def inversionCount(sub1, sub2):

    count = 0
    result = []
    for el in sub1:
        print(el)
        for el2 in sub2:
            if el > el2:
                count +=1 
    result.extend(sub1)
    result.extend(sub2)
    return count, result


def inversion(arr):

    if len(arr) < 2:
        return [0, arr] 
    else:
        mid = len(arr) // 2

        count1, sub1 = inversion(arr[0:mid])
        count2, sub2 = inversion(arr[mid:])
        count, arr = inversionCount(sub1, sub2)
        return [count+count1+count2, arr]

print(inversion([70, 50, 60, 10, 20, 30, 80, 15]))


