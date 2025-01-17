"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = [root]

        while q:
            lvl = q
            q = []
            for i in range(len(lvl)):
                curr = lvl.pop(0)
                if lvl:
                    curr.next = lvl[0]
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root
