class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, 0

        curr_sum = 0

        res = 0

        while r < k:
            curr_sum += nums[r]
            r += 1

        res = curr_sum/k

        while r < len(nums):
            curr_sum -= nums[l]
            curr_sum += nums[r]

            res = max(res, curr_sum/k)

            l += 1
            r += 1

        return res
