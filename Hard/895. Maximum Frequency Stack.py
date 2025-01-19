class FreqStack:

    def __init__(self):
        self.m = defaultdict(int)
        self.freqGroup = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.m[val] += 1
        self.maxFreq = max(self.maxFreq, self.m[val])
        self.freqGroup[self.m[val]].append(val)

    def pop(self) -> int:
        res = self.freqGroup[self.maxFreq].pop()
        self.m[res] -= 1
        if not self.freqGroup[self.maxFreq]:
            self.maxFreq -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
