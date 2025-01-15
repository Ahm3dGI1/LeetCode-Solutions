from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        memo = [[-1 for j in range(len(matrix[0]))]
                for i in range(len(matrix))]
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return 0

            nonlocal res

            if matrix[i][j] == "0":
                return 0

            if memo[i][j] == -1:
                memo[i][j] = min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1)) + 1
            res = max(res, memo[i][j])
            return memo[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)

        return res ** 2
