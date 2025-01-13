class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1, 1

        itr = len(nums)-1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = l
            l = l * nums[i]

        while itr >= 0:
            res[itr] *= r
            r = r * nums[itr]
            itr -= 1

        return res
