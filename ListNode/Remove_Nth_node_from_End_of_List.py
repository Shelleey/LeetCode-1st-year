# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self , head: ListNode , n: int) -> ListNode:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        i = 0
        while i < n:
            i += 1
            fast = fast.next
        while fast is not None:
            fast = fast.next
            if fast is None and slow.next.next is None:
                slow.next = None
                return head
            else:
                slow = slow.next

        slow.val = slow.next.val
        slow.next = slow.next.next
        return head