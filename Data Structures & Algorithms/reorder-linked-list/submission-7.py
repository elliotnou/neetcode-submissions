# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        prev = None
        slow = cur

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        left, right = head, prev
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            left = tmp1
            right.next = left
            right = tmp2
        
        
