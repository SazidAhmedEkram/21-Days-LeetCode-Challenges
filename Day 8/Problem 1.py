class Solution(object):
    def isValid(self, s):
        isValid = False
        stack = ["$"]
        opening = {"(", "{", "["}
        closing = {")", "}", "]"}
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if i == ")":
                    if stack[len(stack) - 1] == "(":
                        stack.pop()
                    else:
                        isValid = False
                        return isValid
                elif i == "}":
                    if stack[len(stack) - 1] == "{":
                        stack.pop()
                    else:
                        isValid = False
                        return isValid
                elif i == "]":
                    if stack[len(stack) - 1] == "[":
                        stack.pop()
                    else:
                        isValid = False
                        return isValid
        if stack[len(stack) - 1] == "$":
            isValid = True
        return isValid