class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1) + 1

        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))

        return res
