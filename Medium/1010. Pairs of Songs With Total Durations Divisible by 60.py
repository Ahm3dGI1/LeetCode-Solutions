class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = {}
        res = 0
        for s in time:
            if s % 60 == 0 and 0 in m:
                res += m[0]

            elif 60 - (s % 60) in m:
                res += m[60 - (s % 60)]

            m[s % 60] = m.get(s % 60, 0) + 1

        return res
