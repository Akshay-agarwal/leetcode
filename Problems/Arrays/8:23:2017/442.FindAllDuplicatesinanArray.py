"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []                     #Result is used to store the duplicates
        for x in nums:                  #Use the array itself as an hash and updaate the numbers we have already seen as item*-1
            if nums[abs(x) - 1] < 0:
                result.append(abs(x))        #If we see again that number as neagitive then append it in the result array
            else:
                nums[abs(x) - 1] *= -1
        return result
