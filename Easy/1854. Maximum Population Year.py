class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []

        for log in logs:
            events.append([log[0], 1])
            events.append([log[1], -1])

        events = sorted(events)
        mx = 0
        res = 0
        curr = 0
        for event in events:
            curr += event[1]
            if curr > mx:
                res = event[0]
                mx = curr

        return res
