# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prov = head.next
        while prov is not None:
            tmp = head.val
            head.val = prov.val
            prov.val = tmp
            if prov.next is not None and prov.next.next is not None:
                head = prov.next
                prov = head.next
            else:
                return dummy.next