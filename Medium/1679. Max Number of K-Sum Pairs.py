class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = {}
        res = 0
        for n in nums:
            if k-n in m and m[k-n] > 0:
                res += 1
                m[k-n] -= 1

            else:
                m[n] = m.get(n, 0) + 1

        return res
