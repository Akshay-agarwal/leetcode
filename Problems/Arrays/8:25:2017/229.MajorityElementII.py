'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Boyer Moore's Algoritham for 2 candidates
        """
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]
