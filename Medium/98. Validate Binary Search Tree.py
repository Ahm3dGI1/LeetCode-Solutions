# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, ma, mi):
            if not root:
                return True
            if root.val <= mi or root.val >= ma:
                return False
            return dfs(root.left, root.val, mi) and dfs(root.right, ma, root.val)

        return dfs(root, 1000000000000, -1000000000000)
