"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Kadane's Algoritham
        """
        max_current, max_global = nums[0], nums[0]              #Initialize current max and global max to the first element
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])   #Check if current max+ nums[i] is greater or the nums[i]
            max_global = max(max_global, max_current)           #Update the global max
        return max_global                                       
