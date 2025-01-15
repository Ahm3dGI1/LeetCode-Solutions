# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def split(self, lis: Optional[ListNode]):
        s = lis
        f = lis.next.next
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        lis1 = lis
        lis2 = s.next
        s.next = None

        return lis1, lis2

    def merge(self, lis1: Optional[ListNode], lis2: Optional[ListNode]):
        dummy = ListNode(0)
        curr = dummy
        while lis1 and lis2:
            if lis1.val < lis2.val:
                curr.next = lis1
                lis1 = lis1.next
            else:
                curr.next = lis2
                lis2 = lis2.next
            curr = curr.next

        if lis1:
            curr.next = lis1

        if lis2:
            curr.next = lis2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        lis1, lis2 = self.split(head)

        lis1 = self.sortList(lis1)
        lis2 = self.sortList(lis2)

        head = self.merge(lis1, lis2)

        return head
