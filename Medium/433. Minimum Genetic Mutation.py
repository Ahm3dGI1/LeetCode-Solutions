class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = [(startGene, 0)]
        done = set()

        while q:
            curr, res = q.pop(0)
            if curr == endGene:
                return res

            for i in range(len(endGene)):
                for c in 'ACGT':
                    if c == curr[i]:
                        continue
                    new = curr[:i] + c + curr[i+1:]
                    if new in bank and new not in done:
                        q.append((new, res+1))
                        done.add(new)

        return -1
