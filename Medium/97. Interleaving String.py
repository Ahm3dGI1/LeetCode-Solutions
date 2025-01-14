class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        memo = [[False] * (m+1) for _ in range(n+1)]

        memo[0][0] = True

        for i in range(1, n+1):
            memo[i][0] = memo[i-1][0] and s1[i-1] == s3[i-1]

        for i in range(1, m+1):
            memo[0][i] = memo[0][i-1] and s2[i-1] == s3[i-1]

        for i in range(1, n+1):
            for j in range(1, m+1):
                memo[i][j] = (memo[i-1][j] and s1[i-1] == s3[i+j-1]
                              ) or (memo[i][j-1] and s2[j-1] == s3[j+i-1])

        return memo[n][m]
