def merge(sub1, sub2):
    a = 0
    b = 0
    result = []
    while a < len(sub1) and b < len(sub2):
        print(a, b)
        if sub1[a] <= sub2[b]:
            result.append(sub1[a])
            a+=1
        else:
            result.append(sub2[b])
            b+=1

    if a < len(sub1):
        for i in range(a, len(sub1)):
            result.append(sub1[i])
    else:
        for i in range(b, len(sub2)):
            result.append(sub2[i])

    return result


def merge_sort(arr):
    print(arr)
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)// 2
        print(mid)
        sub1 = merge_sort(arr[0:mid])
        sub2 = merge_sort(arr[mid:])

        return merge(sub1, sub2)


if __name__ == "__main__":
    print(merge_sort([6, 5, 12, 10, 9, 1]))