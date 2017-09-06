"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"                   #Store all the vowels in a String
        l = list(s)                             #Convert string to a list as its immutable
        i, j = 0, len(l) - 1
        while i < j:
            while i < j and l[i] not in vowels:    #Whenever the value of the list is not vowel increment the pointer
                i += 1
            while i < j and l[j] not in vowels:   #Whenever the value of the list is not vowel decrement the pointer
                j -= 1
            l[i], l[j] = l[j], l[i]               #Exchange the two elements in the list
            i += 1
            j -= 1
        return "".join(l)                          #Convert a list back to a string
