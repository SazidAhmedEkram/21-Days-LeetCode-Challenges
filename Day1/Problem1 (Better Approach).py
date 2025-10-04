class Solution(object):
    def twoSum(self, numbers, target):
        # 1, 2 , 4, 7, 11, 15
        # target = 9
        left = 0
        right = len(numbers) - 1
        while (left < right):
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            elif s < target:
                left += 1
        return None
#Updated
#new feature