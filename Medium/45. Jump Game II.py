class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        near, far = 0, 0
        res = 0

        while far < n-1:
            farthest = 0
            for i in range(near, far+1):
                farthest = max(farthest, i+nums[i])

            near = far+1
            far = farthest
            res += 1

        return res
