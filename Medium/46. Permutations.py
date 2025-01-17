class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def track(i, lis):
            lis.append(nums[i])
            if len(lis) == n:
                res.append(lis.copy())
                return

            for j in range(n):
                if nums[j] not in lis:
                    track(j, lis.copy())
            return

        for i in range(n):
            track(i, [])

        return res
