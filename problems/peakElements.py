def peakElement(array):
    print(array)
    if len(array) > 1:
            i = -1
            c = 0
            j = 1

            while j <= len(array):
                l = float("-inf") if i == -1 else nums[i]
                r = array[j] if j < (len(array)) else float("-inf")
                print(l ,array[c], r)
                if l < array[c] and r < array[c]:
                    return c
                else:
                    i+=1
                    c+=1
                    j+=1
    else:
        return 0
