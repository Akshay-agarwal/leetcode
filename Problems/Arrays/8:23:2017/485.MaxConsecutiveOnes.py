"""
Given a binary array, find the maximum number of consecutive 1s in this array.

"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount, currCount = 0, 0                    #Used to count the max and the curr count of 1's
        for i in range(len(nums)):                    #Iterate the array and check if we have 1 then update the current count
            if nums[i] == 1:
                currCount += 1
                maxCount = max(currCount, maxCount)
            else:
                currCount = 0                         #If we find anything other than 1, make currCount = 0
        return maxCount
