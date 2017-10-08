def merge(l,r):
    result = []
    i,j = 0,0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    if i < len(l):
        result += l[i:]
    else:
        result += r[j:]
    return result

def mergeSort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) // 2
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])
    return merge(l,r)

print(mergeSort([1, 2, 4, 9, 14, 54,5, 6, 7, 8, 11, 12]))