# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we first run a fast and slow pointer that marks the midpoint
        # the fast pointer should start at head.next, we always want the floor
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = slow
        cur = slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # the back half is reversed now, and prev is the head of the right

        left, right = head, prev
        while left:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            left = tmp1
            right.next = left
            right = tmp2
        


