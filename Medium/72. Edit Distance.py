class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memo = [[float(inf)] * (m+1) for _ in range(n+1)]

        def helper(i, j):
            if i == n and j == m:
                return 0
            elif i == n:
                return m - j

            elif j == m:
                return n - i

            if memo[i][j] != float(inf):
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = helper(i+1, j+1)

            else:
                ins = helper(i, j+1) + 1
                rmv = helper(i+1, j) + 1
                swp = helper(i+1, j+1) + 1

                memo[i][j] = min(min(ins, rmv), swp)

            return memo[i][j]

        return helper(0, 0)
