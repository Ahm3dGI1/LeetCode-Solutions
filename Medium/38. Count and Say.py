class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        curr = self.countAndSay(n-1)

        p = 0
        res = ""
        c = 0
        prev = curr[p]
        while p < len(curr):
            if curr[p] == prev:
                c += 1
            else:
                res += str(c) + prev
                c = 1
                prev = curr[p]

            p += 1

        res += str(c) + prev

        return res
