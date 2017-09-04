"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentMin = currentMax = globalMax = nums[0]
        for i in range(1, len(nums)):
            currentMin, currentMax = min(nums[i], nums[i] * currentMax, nums[i] * currentMin), max(nums[i], nums[i] * currentMax, nums[i] * currentMin)
            globalMax = max(globalMax, currentMax)
        return globalMax
