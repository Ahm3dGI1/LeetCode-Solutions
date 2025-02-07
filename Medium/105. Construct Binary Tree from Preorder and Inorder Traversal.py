# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        r = 0
        while r < len(inorder):
            if preorder[0] == inorder[r]:
                break
            r += 1

        root.left = self.buildTree(preorder[1:r+1], inorder[:r])
        root.right = self.buildTree(preorder[r+1:], inorder[r+1:])
        return root
