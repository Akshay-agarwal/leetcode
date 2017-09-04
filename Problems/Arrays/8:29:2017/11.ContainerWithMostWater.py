"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, stop = 0, len(height) - 1                #set two pointers at the start and the end of the array
        maxArea = 0
        while start < stop:
            """
            Calculate the max area for each start and stop till start is less than stop
            """
            maxArea = max(min(height[start], height[stop]) * (stop - start), maxArea)
            if height[start] > height[stop]:            #If height start is greater than stop decrement stop
                stop -= 1
            else:
                start += 1                              #Else increment start
        return maxArea
