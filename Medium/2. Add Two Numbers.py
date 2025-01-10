# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        index, res = 0, 0

        while l1:
            if l1.val == 0:
                l1 = l1.next
                index += 1
                continue
            res += l1.val * (10**index)
            l1 = l1.next
            index += 1

        index = 0

        while l2:
            if l2.val == 0:
                l2 = l2.next
                index += 1
                continue
            res += l2.val * (10**index)
            l2 = l2.next
            index += 1

        tempHead = ListNode(-1)
        curr = tempHead
        index = 1
        print(res)
        if res == 0:
            return ListNode(0)

        while not res == 0:
            rem = (res % (10**index))
            res -= rem
            rem = rem // 10**(index-1)
            curr.next = ListNode(rem)
            curr = curr.next
            index += 1

        return tempHead.next
