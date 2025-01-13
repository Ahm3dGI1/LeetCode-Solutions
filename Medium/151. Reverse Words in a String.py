class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ").trim()

        res = ""
        n = len(arr)

        for i in range(n):
            res += arr[-i-1]
            if i != n-1:
                res += " "

        return res
