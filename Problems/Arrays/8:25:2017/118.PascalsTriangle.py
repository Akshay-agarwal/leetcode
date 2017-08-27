"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:                                        #If row size is zero or less return empty list
            return []
        pascal = [[1]]                                          #Initialize the pascal array with [[1]]
        for i in range(1, numRows):                             #Iterate through the range and add rows to the pascal array
            row = [1 for k in range(i+1)]                       #Create a new array with no of elements of size i and with 1
            j = 1
            while j < i:
                row[j] = pascal[i-1][j-1] + pascal[i-1][j]      #Add the element as pascal[i-1][j-1] + pascal[i-1][j] till j < i
                j += 1
            pascal.append(row)                                  #Append the new row in the pascal array
        return pascal                                           #return pascal array
