"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        Use two pointers and replace the number at the slow pointer,move both the pointers when you find a non zero number
        and also increment both pointers by 1, else just increment the fast pointer
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
