# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyL = ListNode(0, None)
        dummyH = ListNode(0, None)
        dummyC = ListNode(0, head)

        tempL = dummyL
        tempH = dummyH

        curr = dummyC
        while curr.next:
            while curr.next and curr.next.val < x:
                tempL.next = curr.next
                curr.next = curr.next.next
                tempL = tempL.next
                tempL.next = None
            while curr.next and curr.next.val >= x:
                tempH.next = curr.next
                curr.next = curr.next.next
                tempH = tempH.next
                tempH.next = None

        tempL.next = dummyH.next

        return dummyL.next
