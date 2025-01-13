class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, 0
        vowels = 'aeoui'
        res = 0

        while r < k:
            if s[r] in vowels:
                res += 1
            r += 1

        curr = res

        while r < len(s):
            if s[l] in vowels:
                curr -= 1

            if s[r] in vowels:
                curr += 1

            res = max(res, curr)

            l += 1
            r += 1

        return res
