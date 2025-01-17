class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def solve(i, arr):
            nonlocal res
            if len(arr) >= k:
                res.append(arr[:])
                return

            for num in range(i, n+1):
                arr.append(num)
                solve(num+1, arr)
                arr.pop()

        solve(1, [])
        return res
