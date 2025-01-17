# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]

        res = []

        while q:
            s = 0
            l = len(q)
            for _ in range(l):
                curr = q.pop(0)
                s += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(round(s/l, 5))

        return res
