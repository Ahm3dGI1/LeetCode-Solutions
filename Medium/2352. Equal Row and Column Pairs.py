class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c, r = [], []
        n = len(grid)

        for i in range(n):
            currc = []
            currr = []

            for j in range(n):
                currr.append(grid[i][j])
                currc.append(grid[j][i])

            r.append(currr)
            c.append(currc)

        res = 0

        for row in r:
            for col in c:
                if row == col:
                    res += 1

        return res
