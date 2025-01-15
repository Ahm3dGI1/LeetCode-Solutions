class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        m = defaultdict(int)

        curr = rounds[0]
        m[rounds[0]] += 1

        freq = 1

        for i in range(1, len(rounds)):
            while curr != rounds[i]:
                curr += 1
                if curr > n:
                    curr = 1
                m[curr] += 1
                freq = max(freq, m[curr])
        res = []

        for key in m:
            if m[key] == freq:
                res.append(key)

        res.sort()

        return res
