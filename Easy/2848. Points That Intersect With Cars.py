class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        prefix = [0] * 101

        for num in nums:
            for i in range(num[0], num[1]+1):
                prefix[i] = 1

        return sum(prefix)
