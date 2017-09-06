"""
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        for i in range(len(l)):
            l[i] = self.reverse(l[i])
        return " ".join(l)

    def reverse(self, s):
        l = list(s)
        i,j = 0, len(l) - 1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return "".join(l)
