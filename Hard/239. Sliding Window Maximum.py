class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])

        res.append(q[0])

        for i in range(k, len(nums)):
            if q[0] == nums[i-k]:
                q.popleft()
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])

        return res
