'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.
'''
"""
Two ways in whcih this problem can be solved:
1.Sort the array and check max of (largest 3, smallest 2 and largest)
2. Store largest 3 and smallest 2 numbers while traversing, and check max of (largest 3, smallest 2 and largest)
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        large, larger, largest, small, smallest = float('-inf'), float('-inf'), float('-inf'), float('inf'),float('inf')
        for num in nums:
            if num <= smallest:
                    small = smallest
                    smallest = num
            elif num <= small:
                    small = num
            if num >= largest:
                large = larger
                larger = largest
                largest = num
            elif num >= larger:
                large = larger
                larger = num
            elif num >= large:
                large = num
        return max(large * larger * largest, small * smallest * largest)
