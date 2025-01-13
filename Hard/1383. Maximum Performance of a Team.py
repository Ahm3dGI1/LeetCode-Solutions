class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        total = 0
        se = sorted(zip(efficiency, speed), reverse=True)
        pq = []
        ans = 0

        for i in se:
            total += i[1]

            while len(pq) >= k:
                total -= heapq.heappop(pq)

            ans = max(ans, i[0] * total)
            heapq.heappush(pq, i[1])

        return ans % (10**9 + 7)
