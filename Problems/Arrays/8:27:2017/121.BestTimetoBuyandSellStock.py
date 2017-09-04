"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit = 0                                     #Profit should be maximum
        buyPrice = prices[0]                              #BuyPrice should be minimum
        for i in range(1,len(prices)):
            currProfit = prices[i] - buyPrice             #Iterate through the array
            maxProfit = max(currProfit, maxProfit)        #Calculate the maxProfit
            buyPrice = min(buyPrice, prices[i])           #Check for the min Price
        return maxProfit                                  #return maxProfit
