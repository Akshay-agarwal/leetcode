class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = 0
        res = []
        for digit in digits:
            sum = (sum * 10) + digit
        sum += 1
        while sum > 0:
            res.append(sum % 10)
            sum = sum // 10

        return res[::-1]