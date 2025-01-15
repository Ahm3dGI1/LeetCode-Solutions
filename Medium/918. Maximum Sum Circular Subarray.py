class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = 0
        mi = 0
        globalmin = 30**4
        total = 0
        res = -30**4
        for num in nums:
            total += num

            mi = min(mi+num, num)
            m = max(m+num, num)
            res = max(m, res)
            globalmin = min(mi, globalmin)

        if res < 0:
            return res

        return max(total-globalmin, res)
