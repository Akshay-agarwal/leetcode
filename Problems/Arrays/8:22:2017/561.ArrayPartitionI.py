"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n
as large as possible.
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()                             #Sort the nums array
        sum = 0                                 #Initialize sum with 0
        for i in range(0, len(nums)-1, 2):      #Now iterate through the array by taking 2 elements at a time
            sum += min(nums[i], nums[i+1])      #Add the min of these two to the sum
        return sum
