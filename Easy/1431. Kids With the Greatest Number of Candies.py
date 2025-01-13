class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = 0

        for c in candies:
            if c > m:
                m = c

        res = []

        for c in candies:
            if c+extraCandies >= m:
                res.append(True)
            else:
                res.append(False)

        return res
