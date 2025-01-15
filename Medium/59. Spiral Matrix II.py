class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        sr, sc, er, ec = 0, 0, n-1, n-1
        curr = 1
        res = [[0 for i in range(n)] for i in range(n)]

        while sr <= er and sc <= ec:
            for i in range(sc, ec+1):
                res[sr][i] = curr
                curr += 1

            sr += 1

            for i in range(sr, er+1):
                res[i][ec] = curr
                curr += 1

            ec -= 1

            if sr <= er:
                for i in range(ec, sc-1, -1):
                    res[er][i] = curr
                    curr += 1

                er -= 1

            for i in range(er, sr-1, -1):
                res[i][sc] = curr
                curr += 1

            sc += 1

        return res
