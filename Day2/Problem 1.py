class Solution(object):
    def plusOne(self, digits):
        num = ""
        for i in digits:
            num += str(i)
        intNum = int(num)
        finalNum = intNum + 1
        l = len(str(finalNum))
        result = []
        while True:
            result.append(finalNum % 10)
            finalNum = finalNum // 10
            if finalNum == 0:
                break
        result.reverse()
        return result

Solution = Solution()
print(Solution.plusOne([9, 9, 9]))