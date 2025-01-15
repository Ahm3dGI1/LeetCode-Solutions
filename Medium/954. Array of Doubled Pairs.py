class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        m = {}
        res = 0

        arr.sort()

        for s in arr:
            if s/2 in m and m[s/2] > 0:
                res += 1
                m[s/2] -= 1
                m[s] = m.get(s, 0)-1

            elif s*2 in m and m[s*2] > 0:
                res += 1
                m[s*2] -= 1
                m[s] = m.get(s, 0)-1

            m[s] = m.get(s, 0)+1

        return res == len(arr)//2
