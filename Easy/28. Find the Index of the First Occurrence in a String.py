class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = 0
        n = 0

        m = len(haystack)
        t = len(needle)

        while h < m:
            if n == t:
                return h-n
            if haystack[h] == needle[n]:
                n += 1
                h += 1

            else:
                h -= (n-1)
                n = 0

        return h-n if n == t else -1
