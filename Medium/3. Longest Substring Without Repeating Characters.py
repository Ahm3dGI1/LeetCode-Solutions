class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0

        l = 0
        r = 1
        m = 1

        while (r < n):
            if (s[r] in s[l:r]):
                if (r-l+1) > m:
                    m = r-l
                while (s[r] in s[l:r]) and l < r:
                    l += 1
            r += 1
        if (r-l+1) > m:
            m = r-l
        return m
