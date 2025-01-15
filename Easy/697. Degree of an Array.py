class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0

        degree = 0
        c = defaultdict(int)

        for i in nums:
            c[i] += 1
            degree = max(degree, c[i])

        res = 50000
        m = defaultdict(int)

        while l <= r and r < len(nums):
            m[nums[r]] += 1
            while m[nums[r]] == degree:
                res = min(res, (r-l) + 1)
                m[nums[l]] -= 1
                l += 1

            r += 1

        return res
