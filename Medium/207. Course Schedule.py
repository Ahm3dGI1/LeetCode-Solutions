class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i: [] for i in range(numCourses)}
        visit = set()

        for c, p in prerequisites:
            m[c].append(p)

        def check(course):
            if not m[course]:
                return True

            if course in visit:
                return False
            visit.add(course)

            for c in m[course]:
                if not check(c):
                    return False
            m[course] = []

            return True

        for i in range(numCourses):
            if not check(i):
                return False

        return True
