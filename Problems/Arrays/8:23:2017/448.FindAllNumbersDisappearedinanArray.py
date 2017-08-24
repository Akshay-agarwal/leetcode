"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Use the items in the list and update the list so that all the elements in the list except for those at the missing
        position are neagitive. Then iterate through the updated array and get the positive numbers
        """
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i+1 for i in range(n) if nums[i] > 0]
