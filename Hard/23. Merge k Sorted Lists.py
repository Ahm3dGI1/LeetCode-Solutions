# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, lis1, lis2):
        res = ListNode(0)
        curr = res

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

        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        r = len(lists)
        mid = r//2

        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
