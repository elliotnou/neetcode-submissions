# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge cases:
            # first node is removed -- need a dummy pointer whose next is head
        
        dummy = ListNode()
        dummy.next = head

        end = cur = dummy

        while n >= 0:
            end = end.next
            n -= 1
        
        while end:
            cur = cur.next
            end = end.next

        cur.next = cur.next.next

        return dummy.next
        