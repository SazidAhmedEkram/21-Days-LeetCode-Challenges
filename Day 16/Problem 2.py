class Solution(object):
    def pivotIndex(self, nums):
        found = False
        for i in range(len(nums)):
            if i == 0 and sum(nums[i+1:]) == 0:
                return 0
            if i == len(nums) - 1 and sum(nums[:i]) == 0:
                return len(nums) - 1
            if sum(nums[:i]) == sum(nums[i+1:]):
                found = True
                return i
        if not found:
            return -1