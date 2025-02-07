class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lo, sh = 0, 0

        while lo < len(t) and sh < len(s):
            if t[lo] == s[sh]:
                sh += 1
            lo += 1

        return sh == len(s)
