# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(0, head)
        size = 0
        prev = dummy
        curr = prev.next
        last = None

        temp = head
        while temp:
            size += 1
            temp = temp.next

        for _ in range(size//k):
            for _ in range(k):
                nxt = curr.next
                curr.next = last
                last = curr
                curr = nxt

            temp = prev.next
            prev.next = last
            temp.next = nxt
            prev = temp
            last = None

        return dummy.next
