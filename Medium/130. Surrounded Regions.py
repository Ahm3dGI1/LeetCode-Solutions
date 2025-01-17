class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        n, m = len(board), len(board[0])

        def dfs(i, j):
            if i >= n or i < 0 or j >= m or j < 0 or (i, j) in visited:
                return
            if board[i][j] == 'X':
                return

            visited.add((i, j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)
        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[n-1][i] == 'O':
                dfs(n-1, i)

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    board[i][j] = 'X'

        return board
