class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()

        for s in range(len(senate)):
            if senate[s] == "R":
                r.append(s)

            if senate[s] == "D":
                d.append(s)

        n = len(senate)-1

        while r and d:
            n += 1
            if r[0] < d[0]:
                r.append(n)
            else:
                d.append(n)

            r.popleft()
            d.popleft()

        return "Dire" if d else "Radiant"
