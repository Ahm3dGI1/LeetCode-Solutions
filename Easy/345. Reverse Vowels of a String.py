class Solution:
    def reverseVowels(self, s: str) -> str:
        sta = []

        for c in s:
            if c in "AaEeIiOoUu":
                sta.append(c)

        res = []

        for c in s:
            if c in "AaEeIiOoUu":
                res.append(sta.pop())
                continue
            res.append(c)

        return "".join(res)
