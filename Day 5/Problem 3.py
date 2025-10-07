class Solution(object):
    def threeSum(self, nums):
        threeSum = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    threeSum.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1

        return threeSum
