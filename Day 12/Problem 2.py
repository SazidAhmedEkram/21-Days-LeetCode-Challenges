class Solution(object):
    def isAnagram(self, s, t):
        sArr = []
        tArr = []
        for i in s:
            sArr.append(i)
        for i in t:
            tArr.append(i)
        sArr.sort()
        tArr.sort()
        if sArr == tArr:
            return True
        else:
            return False

solution = Solution()
print(solution.isAnagram("cba", "cbd"))