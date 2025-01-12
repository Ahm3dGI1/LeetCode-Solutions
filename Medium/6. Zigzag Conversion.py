class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""

        for i in range(numRows):
            curr = i
            while curr < len(s):
                res += s[curr]
                if i > 0 and i < numRows-1 and ((curr + (numRows - 1) * 2) - 2*i) < len(s):
                    res += s[(curr + (numRows - 1) * 2) - 2*i]
                curr += (numRows - 1) * 2

        return res
