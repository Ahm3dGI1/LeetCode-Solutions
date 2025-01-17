# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lis = []

        def helper(root):
            if not root:
                return
            nonlocal lis
            lis.append(root)
            helper(root.left)
            helper(root.right)
            return

        helper(root)

        for i in range(len(lis)-1):
            lis[i].right = lis[i+1]
            lis[i].left = None
        if lis:
            lis[-1].right = None
            lis[-1].left = None

        return root
