class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        curr = 0
        res = 10**5+1

        for i in range(len(nums)):
            total += nums[i]
            curr += 1

            while total >= target:
                res = min(res, curr)
                total -= nums[l]
                curr -= 1
                l += 1

        return res if res < 10**5+1 else 0
