class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            ss = str(sorted(s))
            m[ss].append(s)

        res = []

        for key in m:
            res.append(m[key])

        return res
