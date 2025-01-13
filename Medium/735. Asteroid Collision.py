class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for i in asteroids:
            if i < 0:
                while s and s[-1] > 0 and s[-1] < -i:
                    s.pop()

                if not s or s[-1] < 0:
                    s.append(i)

                if s and s[-1] == -i:
                    s.pop()

            else:
                s.append(i)

        return s
