class Solution(object):
    def climbStairs(self, n):
        dp = []
        dp.append(1)
        dp.append(2)
        if n == 1:
            return dp[0]
        if n == 2:
            return dp[1]
        for i in range(2, n):
            dp.append(dp[i-2] + dp[i-1])
        return dp[len(dp) - 1]