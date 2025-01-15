class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        m = set()
        zeros = set()

        res = 0

        for n in nums:
            if n not in m:
                if n-k in m:
                    res += 1

                if n+k in m:
                    res += 1

            if k == 0 and n in m and n not in zeros:
                res += 1
                zeros.add(n)

            m.add(n)

        return res
