class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        res = 0
        for n in nums:
            m[n] = 1

        for n in nums:
            if n not in m:
                continue
            i = 1
            while n + i in m:
                m[n] += m[n+i]
                del m[n+i]
                i += 1
            res = max(res, m[n])

        return res
