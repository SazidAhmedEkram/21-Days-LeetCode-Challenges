class Solution(object):
    def rob(self, nums):
        if nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], nums[i] + dp[i-2]))
        return dp[len(nums) - 1]