# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        size = 0
        first = None
        last = None

        curr = ans = head

        while curr:
            size += 1
            if size == left-1:
                first = curr
            if size == right+1:
                last = curr
            if left == 1 and size == right:
                ans = curr
            curr = curr.next

        size = 0
        curr = head
        prev = last

        while curr:
            size += 1

            nxt = curr.next
            if size >= left and size <= right:
                curr.next = prev
                prev = curr

            curr = nxt

        if first:
            first.next = prev

        return ans
