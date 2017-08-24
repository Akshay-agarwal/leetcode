"""
In MATLAB, there is a very useful function called 'reshape', which can
reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c
representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the
same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums

        result = [[0]* c for k in range(r)]
        row = len(nums)
        col = len(nums[0])
        row_new = 0
        col_new = 0
        for i in range(row):
            for j in range(col):
                result[row_new][col_new] = nums[i][j]
                col_new += 1
                if col_new == c:
                    col_new = 0
                    row_new += 1
        return result
