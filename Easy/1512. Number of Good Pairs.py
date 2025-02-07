class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        check = {}
        res = 0
        for n in nums:
            check[n] = check.get(n, 0)+1
            res += check[n] - 1

        return res
