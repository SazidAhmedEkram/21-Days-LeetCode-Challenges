class Solution(object):
    def singleNumber(self, nums):
        for i in range(0, len(nums)):
             if not(nums[i] in nums[:i] or nums[i] in nums[i+1:]):
                return nums[i]