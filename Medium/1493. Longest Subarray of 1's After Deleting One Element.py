class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        dele = 1

        while r < len(nums):
            if nums[r] == 0:
                dele -= 1

            if dele < 0:
                if l == 0:
                    dele += 1
                l += 1
            r += 1

        return r-l-1
