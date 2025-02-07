class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        l = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if i - l - 1 == 0:
                    res.append(f"{nums[l]}")
                else:
                    res.append(f"{nums[l]}->{nums[i-1]}")

                l = i

        if len(nums) - l - 1 == 0:
            res.append(f"{nums[l]}")
        else:
            res.append(f"{nums[l]}->{nums[len(nums)-1]}")

        return res
