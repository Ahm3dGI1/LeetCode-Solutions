class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        running_sum = 0

        for alr in gain:
            running_sum += alr
            res = max(res, running_sum)

        return res
