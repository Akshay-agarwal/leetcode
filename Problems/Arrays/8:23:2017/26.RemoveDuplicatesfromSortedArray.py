"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:                    #If length of nums is 0 return zero
            return 0
        j = 0
        for i in range(1,len(nums)):    #Iterate through the array from index 1 and check for array item at with item at prev
            if nums[i] != nums[i-1]:
                nums[j+1] = nums[i]     #If they are not equal update j+1 and increment j by 1
                j += 1
        return j + 1
