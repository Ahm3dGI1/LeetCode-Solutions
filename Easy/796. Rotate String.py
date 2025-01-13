class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        if n != len(goal):
            return False

        for i in range(n):
            for j in range(n):
                if s[j] != goal[j-i]:
                    break
                if j == n-1:
                    return True

        return False
