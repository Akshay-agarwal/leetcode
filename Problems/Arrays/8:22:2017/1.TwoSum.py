"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Iterate through the array and store the value of the target-nums[i] in dictionary, if we find the matching value                 return the indexes of the elements
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return (dict[nums[i]],i)
            else:
                dict[target - nums[i]] = i
