# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(root, res):
            if not root:
                return 0

            if not root.left and not root.right:
                return (res * 10) + root.val

            return helper(root.left, (res * 10) + root.val) + helper(root.right, (res * 10) + root.val)

        return helper(root, 0)
