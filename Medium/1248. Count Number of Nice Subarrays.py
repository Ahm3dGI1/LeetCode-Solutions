class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, m, r = 0, 0, 0

        od = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] % 2:
                od += 1

            while od > k:
                if nums[l] % 2:
                    od -= 1
                l += 1
                m = l

            if od == k:
                while not nums[m] % 2:
                    m += 1

                res += m - l + 1

        return res
