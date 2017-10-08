def BinarySearch(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

arr = [1,2,3,4,5,6,7,8]
print(BinarySearch(arr, 68))