"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?


"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(0, rowIndex+1):                          #Iterate through the range and add rows to the pascal array
            temp = [1 for k in range(i+1)]                      #Create a temp array with no of elements of size i+1 and with 1
            j = 2
            while j < i+1:
                temp[j-1] = curr[j-2] + curr[j-1]               #Add the element as temp[j-1] + temp [j-2] till it is < i+1
                j += 1                                          #Increment j
            curr = temp                                         #store the temp in curr
        return curr
