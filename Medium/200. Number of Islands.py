class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range((n)):
            for j in range((m)):
                if grid[i][j] == '0':
                    continue
                dfs(i, j)
                res += 1

        return res
