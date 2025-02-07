class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = [points[0]]

        for s, e in points[1:]:
            if s <= res[-1][1]:
                res[-1][0] = max(res[-1][0], s)
                res[-1][1] = min(res[-1][1], e)
            else:
                res.append([s, e])

        return len(res)
