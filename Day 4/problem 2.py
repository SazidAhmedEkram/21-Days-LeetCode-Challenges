class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for i in range(0, len(nums)):
            if s.__contains__(nums[i]):
                return True
            else:
                s.add(nums[i])
        return False

