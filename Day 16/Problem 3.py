class Solution(object):
    def productExceptSelf(self, nums):
        ans = []
        mul = 1
        zero = 1
        get = False
        k = 0
        for i in nums:
            mul *= i
            if i == 0:
                k += 1
                continue
            else:
                zero *= i
                get = True

        if not get or k > 1:
            zero = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                temp = zero
            else:
                temp = mul / nums[j]
            ans.append(temp)
        return ans