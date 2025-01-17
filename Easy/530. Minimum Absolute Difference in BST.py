# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        tree = []

        def dfs(root):
            nonlocal tree
            if not root:
                return

            dfs(root.left)
            tree.append(root.val)
            dfs(root.right)

            return

        dfs(root)
        res = float('inf')

        for i in range(1, len(tree)):
            res = min(res, tree[i]-tree[i-1])

        return res
