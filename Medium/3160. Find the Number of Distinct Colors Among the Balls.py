class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        b = {}
        c = {}
        res = []
        curr = 0
        for q in queries:
            if q[0] in b:
                c[b[q[0]]] -= 1

                if c[b[q[0]]] == 0:
                    curr -= 1

            b[q[0]] = q[1]

            if q[1] not in c or c[q[1]] == 0:
                curr += 1
            c[q[1]] = c.get(q[1], 0) + 1

            res.append(curr)
        return res
