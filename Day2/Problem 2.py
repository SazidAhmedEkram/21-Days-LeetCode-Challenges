class Solution(object):
    def maxProfit(self, prices):
        minimumPrice, maximumProfit = prices[0], 0
        for i in range(1, len(prices)):
            if minimumPrice > prices[i]:
                minimumPrice = prices[i]
            if maximumProfit < prices[i] - minimumPrice:
                maximumProfit = prices[i] - minimumPrice
        return maximumProfit

solution = Solution()
print(solution.maxProfit([1]))