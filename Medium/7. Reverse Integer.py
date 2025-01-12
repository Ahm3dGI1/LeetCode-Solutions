class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x
        res = ""
        x = str(x)

        for c in x:
            res = c + res

        res = int(res)

        if res >= 2**31:
            return 0

        return res if not neg else -res
