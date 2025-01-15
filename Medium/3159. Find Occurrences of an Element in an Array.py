class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        res = []
        lis = []

        for n in range(len(nums)):
            if nums[n] == x:
                lis.append(n)

        for q in queries:
            if q > len(lis):
                res.append(-1)
            else:
                res.append(lis[q-1])

        return res
