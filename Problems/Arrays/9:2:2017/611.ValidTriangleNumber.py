"""
Given an array consists of non-negative integers, your task is to count the number of triplets
chosen from the array that can make triangles if we take them as side lengths of a triangle.
"""
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        if len(nums) < 3:
            return sum
        nums.sort()
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    sum += right - left
                    right -= 1
                else:
                    left += 1
        return sum
