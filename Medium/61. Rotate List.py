# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        last = None
        before = None
        target = None

        size = 0
        temp = head
        while temp:
            size += 1
            if temp and not temp.next:
                last = temp
            temp = temp.next

        k = k % size

        if k == 0:
            return head

        dummy = ListNode(0, head)
        temp = head

        while temp:
            size -= 1
            if size == k:
                before = temp
            elif size == k-1:
                target = temp
            temp = temp.next

        before.next = None
        last.next = dummy.next
        dummy.next = target

        return dummy.next
