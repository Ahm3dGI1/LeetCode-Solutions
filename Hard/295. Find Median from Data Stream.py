class MedianFinder:

    def __init__(self):
        self.mi_pq = []
        self.ma_pq = []

    def addNum(self, num: int) -> None:
        if not self.ma_pq:
            if not self.mi_pq or self.mi_pq[0] > num:
                heapq.heappush(self.ma_pq, -num)
            else:
                heapq.heappush(self.ma_pq, -heapq.heappop(self.mi_pq))
                heapq.heappush(self.mi_pq, num)
            pass

        elif not self.mi_pq:
            if not self.ma_pq or -self.ma_pq[0] < num:
                heapq.heappush(self.mi_pq, num)
            else:
                heapq.heappush(self.mi_pq, -heapq.heappop(self.ma_pq))
                heapq.heappush(self.ma_pq, -num)
            pass

        elif len(self.mi_pq) == len(self.ma_pq):
            if self.mi_pq[0] < num:
                heapq.heappush(self.mi_pq, num)

            else:
                heapq.heappush(self.ma_pq, -num)

            pass

        elif len(self.mi_pq) > len(self.ma_pq):
            if self.mi_pq[0] < num:
                heapq.heappush(self.ma_pq, -heapq.heappop(self.mi_pq))
                heapq.heappush(self.mi_pq, num)

            else:
                heapq.heappush(self.ma_pq, -num)

            pass

        elif len(self.mi_pq) < len(self.ma_pq):
            if -self.ma_pq[0] > num:
                heapq.heappush(self.mi_pq, -heapq.heappop(self.ma_pq))
                heapq.heappush(self.ma_pq, -num)

            else:
                heapq.heappush(self.mi_pq, num)

            pass

    def findMedian(self) -> float:
        if len(self.ma_pq) == len(self.mi_pq):
            return (-self.ma_pq[0] + self.mi_pq[0])/2

        elif len(self.ma_pq) > len(self.mi_pq):
            return -self.ma_pq[0]

        else:
            return self.mi_pq[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
