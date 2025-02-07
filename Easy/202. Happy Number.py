class Solution:
    def isHappy(self, n: int) -> bool:
        s = []
        curr = n
        while curr not in s:
            if curr == 1:
                return True
            s.append(curr)
            temp = 0
            for c in str(curr):
                temp += int(c)**2

            curr = temp

        return False
