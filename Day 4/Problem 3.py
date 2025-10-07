class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]

        for i in range(0, len(nums) - 1):
            sub = []
            sub.append(nums[i])
            for j in range(i + 1, len(nums)):
                sub.append(nums[j])
                if maxSum < sum(sub):
                    maxSum = sum(sub)
                    print(maxSum)
                else:
                    break
        return maxSum

solution = Solution()
print(solution.maxSubArray([5,4,-1,7,8]))