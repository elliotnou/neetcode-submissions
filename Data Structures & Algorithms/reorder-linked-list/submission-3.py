# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we run a slow and fast pointer to find the midpoint+1 (?) 
        # we reverse the back half, i.e. starting from slow pointer

        # then, we traverse from head forward and end backwards to connect the linked list

        # [2, 4, 6, 8]
        dummy = head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow lands in the midpoint, the NEXT should be reversed
        cur = slow.next
        slow.next = None
        right = None
        while cur:
            temp = cur.next
            cur.next = right
            right = cur
            cur = temp
        
        # the right half has been reversed
        left = head
        while left and right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            left = tmp1
            right.next = left
            right = tmp2
        
