class Solution(object):
    def searchRange(self, arr, target):
        if not arr:
            return [-1, -1]
        start = self.BinarySearch(arr, target - 0.5)
        if arr[start] != target:
            return [-1, -1]
        arr.append(0)
        end = self.BinarySearch(arr, target + 0.5) - 1
        return [start, end]

    def BinarySearch(self, nums, target):
        low, high = 0, len(nums) - 1
        while high > low:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return low