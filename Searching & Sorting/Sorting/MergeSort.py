def merge(l,r):
    print(l,r)
    result = []
    i, j = 0,0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    print(arr[mid:], arr[:mid])
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])
    return merge(l,r)

print(mergeSort([1,4,2,9,14,54,6,5,8,12,11,7]))