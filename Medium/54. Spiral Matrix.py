class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        sr, sc, er, ec = 0, 0, row-1, col-1

        res = []
        while sr <= er and sc <= ec:
            for i in range(sc, ec+1):
                res.append(matrix[sr][i])

            sr += 1

            for i in range(sr, er+1):
                res.append(matrix[i][ec])

            ec -= 1

            if sr <= er:
                for j in range(ec, sc - 1, -1):
                    res.append(matrix[er][j])
                er -= 1

            if sc <= ec:
                for i in range(er, sr - 1, -1):
                    res.append(matrix[i][sc])
                sc += 1

        return res
