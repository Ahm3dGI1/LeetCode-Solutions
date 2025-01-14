class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        projects = 0
        prev = 0
        keys = sorted(zip(capital, profits))

        while projects < k:

            while prev < len(keys) and keys[prev][0] <= w:
                heapq.heappush(pq, -keys[prev][1])
                prev += 1

            if not pq:
                break
            w += - heapq.heappop(pq)
            projects += 1

        return w
