"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""
"""
1. First multiply all elements on the left
2. Next multiply all elements on the right
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * p
            p *= nums[i]
        return output
