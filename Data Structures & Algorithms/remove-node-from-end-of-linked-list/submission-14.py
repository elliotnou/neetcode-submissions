# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # nth node from end, means we need to traverse the whole list once with two pointers, the one AHEAD being 

        behind = ListNode()
        behind.next = head
        dummy = ahead = behind

        while n > 0:
            ahead = ahead.next
            n -= 1
        
        while ahead and ahead.next:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next
        
