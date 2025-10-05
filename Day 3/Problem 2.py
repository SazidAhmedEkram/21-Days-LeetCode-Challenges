class Solution(object):
    def toLowerCase(self, s):
        lower = ""
        for i in s:
            if i.isupper():
                lower += i.lower()
            else:
                lower += i
        return lower