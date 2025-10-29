class Solution(object):
    def matrixReshape(self, mat, r, c):
        total = sum(len(row) for row in mat)
        if r * c != total:
            return mat
        arr = [[None] * c for i in range(r)]
        a = 0
        b = 0
        for i in mat:
            for j in i:
                arr[a][b] = j
                if b < c - 1:
                    b += 1
                else:
                    a += 1
                    b = 0
        return arr

solution = Solution()
print(solution.matrixReshape([[1,2],[3,4]], 4, 1))