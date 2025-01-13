class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        s = set()
        l = 0

        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        for k in freq:
            s.add(freq[k])
            l += 1

        return l == len(s)
