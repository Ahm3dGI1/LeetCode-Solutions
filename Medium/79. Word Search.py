class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.solve(board, word, 0, i, j):
                    return True
        return False

    def solve(self, board: list[list[str]], word: str, check: int, row: int, col: int) -> bool:
        if check >= len(word):
            return True

        if (row < 0 or col < 0 or
            row >= len(board) or col >= len(board[0]) or
                board[row][col] != word[check]):
            return False

        temp = board[row][col]
        board[row][col] = '#'

        found = (self.solve(board, word, check + 1, row + 1, col) or
                 self.solve(board, word, check + 1, row - 1, col) or
                 self.solve(board, word, check + 1, row, col + 1) or
                 self.solve(board, word, check + 1, row, col - 1))

        board[row][col] = temp
        return found
