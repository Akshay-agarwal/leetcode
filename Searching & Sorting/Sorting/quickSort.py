from random import randint

def getPivot(low, high):
    return randint(low, high)

def quickSort(arr):
    return quickSort2(arr, 0, len(arr)-1)

def quickSort2(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort2(arr, low, p-1)
        quickSort2(arr, p+1, high)

    return arr

def partition(arr, low, high):
    pivotIndex = getPivot(low, high)
    pivot = arr[pivotIndex]
    arr[low], arr[pivotIndex] = arr[pivotIndex], arr[low]
    border = low

    for i in range(low+1, high+1):
        if arr[i] < pivot:
            border += 1
            arr[border], arr[i] = arr[i], arr[border]

    arr[border], arr[low] = arr[low], arr[border]

    return border

print(quickSort([12,34,23,5,4,2443,2323,45653,234,2]))