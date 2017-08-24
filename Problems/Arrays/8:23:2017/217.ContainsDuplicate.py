"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:                    #if nums is empty return False
            return False

        d = {}                          #Create a new dictionary and add elements of the array in it
        for i in range(len(nums)):
            if nums[i] not in d:        #If we a new number add it to dictionary
                d[nums[i]] = 1
            else:
                return True             #If the number is already in dictionary return True
        return False
