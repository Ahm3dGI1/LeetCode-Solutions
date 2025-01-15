class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, arr, s):
            if s == target:
                nonlocal res
                res.append(arr)
                return
            if s > target:
                return

            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                dfs(i, arr[:], s+candidates[i])
                arr.pop()

        dfs(0, [], 0)

        return res
