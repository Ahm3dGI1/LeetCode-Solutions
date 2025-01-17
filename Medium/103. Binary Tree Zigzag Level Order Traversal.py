# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]

        res = []

        while q:
            lvl = []
            for _ in range(len(q)):
                curr = q.pop(0)
                lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if lvl:
                res.append(lvl)

            lvl = []
            for _ in range(len(q)):
                curr = q.pop(0)
                lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if lvl:
                for i in range(len(lvl)//2):
                    lvl[-i-1], lvl[i] = lvl[i], lvl[-i-1]
                res.append(lvl)

        return res
