"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Since Strings are immutable first convert String to a list
        """
        listString = list(s)
        i,j = 0,len(listString)-1
        while i < j:                                        #Now interchange the i & j from front and back.
            listString[i], listString[j] = listString[j], listString[i]
            i += 1
            j -= 1
        return "".join(listString) #join the elements of the array to form a string again.
