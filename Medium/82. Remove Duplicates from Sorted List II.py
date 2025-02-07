# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        temp = dummy
        curr = temp.next.next

        while curr:
            if temp.next.val == curr.val:
                while curr and temp.next.val == curr.val:
                    curr = curr.next
                temp.next = curr
                if curr:
                    curr = curr.next

            else:
                temp = temp.next
                curr = curr.next

        return dummy.next
