class Solution(object):
    def isHappy(self, n):
        while n not in [2, 3, 4, 5, 6, 7, 8, 9]:
            sumofsquare = 0
            for i in str(n):
                sumofsquare += int(i) * int(i)

            if sumofsquare == 1:
                return True
            else:
                print(sumofsquare)
                n = sumofsquare
        return False


s = Solution()
print(s.isHappy(2))