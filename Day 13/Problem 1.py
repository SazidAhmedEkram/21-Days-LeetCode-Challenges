class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        stack.append("$")
        for i in s:
            if stack[len(stack) - 1] == i:
                stack.pop()
            else:
                stack.append(i)
        stack.remove("$")
        return "".join(stack)
