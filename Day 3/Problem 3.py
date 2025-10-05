class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        substring = ""
        c = 0
        i = 0
        while c != len(s) and s != "":
            if s[i] in substring:
                substring = ""
                substring += s[i]
            else:
                substring += s[i]
            i = i + 1
            length = len(substring)
            if maxLength < length:
                maxLength = length

            if i == len(s):
                c = c + 1
                i = c
                substring = ""
        return maxLength

solution = Solution()
print(solution.lengthOfLongestSubstring(""))