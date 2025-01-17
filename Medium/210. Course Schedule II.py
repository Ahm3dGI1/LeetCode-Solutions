class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = {i: [] for i in range(numCourses)}
        res = []
        visit = set()

        for c, p in prerequisites:
            m[c].append(p)

        def dfs(course):
            if course in visit:
                return []

            visit.add(course)

            for co in m[course]:
                if dfs(co) == []:
                    return []

            visit.remove(course)
            m[course] = []
            if course not in res:
                res.append(course)
            return res

        for i in range(numCourses):
            if dfs(i) == []:
                return []

        return res
