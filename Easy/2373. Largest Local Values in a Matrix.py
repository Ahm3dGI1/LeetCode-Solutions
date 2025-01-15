class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        res = [[0 for i in range(m-2)]for i in range(n-2)]

        def check(i, j):
            res = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    res = max(res, grid[k][l])

            return res

        for i in range(1, n-1):
            for j in range(1, m-1):
                res[i-1][j-1] = check(i, j)

        return res
