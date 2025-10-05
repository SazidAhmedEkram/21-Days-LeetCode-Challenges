class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        left = right = 0
        substring = []
        for i in range(0, len(s)):
            if s[i] in substring:
                while s[i] in substring:
                    j = 0
                    substring.remove(substring[j])
                    j += 1
                    left += 1
                right += 1
                substring.append(s[i])
            else:
                substring.append(s[i])
                right += 1
            print(substring)
            length = right - left
            if maxLength < length:
                maxLength = length
        return maxLength

s = Solution()
print(s.lengthOfLongestSubstring(""))
