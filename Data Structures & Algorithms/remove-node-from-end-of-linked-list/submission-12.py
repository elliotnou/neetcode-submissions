# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # since its from the end of the list, we have two pointers that maintaini a distance of 2 and when the furtehr pointer reaches the end, remove that. btu we ned knoweldge of the node BEFOE the one to remove, so while fast, fast.next

        left = right = ListNode(0, head)
        dummy = left
        while n:
            right = right.next
            n -= 1

        while right and right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
    

        

        

