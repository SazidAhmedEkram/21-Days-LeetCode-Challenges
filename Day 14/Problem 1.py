class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(len(prices)):
            if profit < prices[i] - buy:
                profit = prices[i] - buy
            if buy > prices[i]:
                buy = prices[i]
        return profit