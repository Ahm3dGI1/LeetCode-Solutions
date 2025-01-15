class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = 0
        res = -10**4
        for num in nums:
            m += num
            m = max(m, num)
            res = max(m, res)

        return res
