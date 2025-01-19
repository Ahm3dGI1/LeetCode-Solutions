class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0]*n

        def helper(curr, s):
            if int(curr) > int("26") or int(curr[0]) == int("0"):
                return 0
            if memo[len(s)]:
                return memo[len(s)]

            if not s:
                memo[len(s)] = 1
                return memo[len(s)]

            if len(s) >= 1:
                memo[len(s)] += helper(s[:1], s[1:])
            if len(s) >= 2:
                memo[len(s)] += helper(s[:2], s[2:])

            return memo[len(s)]

        one = two = 0
        if n >= 1:
            one = helper(s[:1], s[1:])
        if n >= 2:
            two = helper(s[:2], s[2:])

        return one + two
