class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        while i < n and s[i] == " ":
            i += 1

        if i >= n or s[i] not in "+-0123456789":
            return res

        sign = 1

        if i < n and s[i] in "+-":
            if s[i] == '-':
                sign = -sign
            i += 1

        if i >= n or s[i] not in "0123456789":
            return res

        while i < n and s[i] == "0":
            i += 1

        while i < n and s[i] in "0123456789":
            res *= 10
            res += int(s[i])
            i += 1

        res *= sign

        if res < -2**31:
            return -2**31
        elif res >= 2**31:
            return (2**31) - 1
        else:
            return res
