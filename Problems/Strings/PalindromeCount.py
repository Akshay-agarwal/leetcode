class Solution(object):
    def palindromSubstring(self,s):
        if len(s) == 0 or len(s) == 1:
            return len(s)
        lengthOfString = len(s)
        palindromeTable = [[None for j in range(lengthOfString)] for i in range(lengthOfString)]
        count = 0
        for i in range(lengthOfString):
            palindromeTable[i][i] = True
            count += 1
        for i in range(1,lengthOfString):
            if s[i] == s[i - 1]:
                palindromeTable[i - 1][i] = True
                count += 1
                print(count,2)
        for k in range(3,lengthOfString+1):
            for i in range(lengthOfString-k+1):
                j = i + k -1
                if palindromeTable[i+1][j-1] == True and s[i] == s[j]:
                    palindromeTable[i][j] = True
                    count += 1
        print(count)

s = Solution()
a = s.palindromSubstring("hellolle")
print(a)

