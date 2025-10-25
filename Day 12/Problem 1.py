class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        isPlaindrome = True
        while i < j:
            if not(65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57):
                i += 1
                continue
            if not(65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122 or 48 <= ord(s[j]) <= 57):
                j -= 1
                continue
            if 48 <= ord(s[i]) <= 57:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    isPlaindrome = False
                    break
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    isPlaindrome = False
                    break
        return isPlaindrome


solution = Solution()
print(solution.isPalindrome("p0"))