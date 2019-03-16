# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prov = head.next

        if prov.val != head.val:
            head.next = self.deleteDuplicates ( prov )
            return head

        while prov is not None and prov.val == head.val:
            prov = prov.next
        return self.deleteDuplicates ( prov )