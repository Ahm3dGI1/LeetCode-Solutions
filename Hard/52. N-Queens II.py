class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        r_dia = set()
        l_dia = set()

        def backtrack(i):
            if i == n:
                return 1

            res = 0

            for c in range(n):
                if c in col or (i - c) in r_dia or (i + c) in l_dia:
                    continue

                col.add(c)
                r_dia.add(i-c)
                l_dia.add(i+c)

                res += backtrack(i+1)

                col.remove(c)
                r_dia.remove(i-c)
                l_dia.remove(c+i)

            return res

        return backtrack(0)
