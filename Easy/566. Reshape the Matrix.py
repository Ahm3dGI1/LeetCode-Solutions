class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        n, m = len(mat), len(mat[0])

        if r*c != m*n:
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        cr, cc, cn, cm = 0, -1, 0, -1

        for i in range(r*c):
            cc += 1
            cm += 1

            if cc >= c:
                cr += 1
                cc = 0

            if cm >= m:
                cn += 1
                cm = 0

            res[cr][cc] = mat[cn][cm]

        return res
