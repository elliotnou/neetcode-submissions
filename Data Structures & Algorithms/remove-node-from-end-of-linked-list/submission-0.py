# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ret = head
        # two pointers, prev and end, create a gap of n.
        # if end.next is None, 

        prev = ret = ListNode()
        prev.next = ret.next = head
        end = head
        for _ in range(n):
            end = end.next
        
        while end:
            end = end.next
            prev = prev.next

        
        print(head.val)
        prev.next = prev.next.next

        return ret.next