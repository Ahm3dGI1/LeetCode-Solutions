class RecentCounter:

    def __init__(self):
        self.p = deque()

    def ping(self, t: int) -> int:
        self.p.append(t)
        while t-3000 > self.p[0]:
            self.p.popleft()
        return len(self.p)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
