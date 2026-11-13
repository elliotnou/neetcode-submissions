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
        
        # at the midpoint. start reversing
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        

        left = head
        right = prev
        while left and right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            left = tmp1
            right.next = left
            right = tmp2
        

