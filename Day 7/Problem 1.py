class Solution(object):
    def generate(self, numRows):
        output = [[1]]
        k = 1
        while k < numRows:
            k += 1
            sub = []
            for i in range(0, len(output[len(output) - 1]) + 1):
                if i == 0:
                    sub.append(1)
                elif i == len(output[len(output) - 1]):
                    sub.append(1)
                else:
                    sub.append(output[len(output) - 1][i] + output[len(output) - 1][i - 1])
            output.append(sub)
        return output