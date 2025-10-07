class Solution(object):
    def maxSubArray(self, nums):
        currentSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))