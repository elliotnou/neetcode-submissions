# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use two pointers
        left = head
        length = 0
        count = head
        while count.next:
            count = count.next
            length += 1
        
        rev = head
        # put start of reverse at the middle
        for _ in range(length // 2):
            rev = rev.next
        
        right = None
        # reverse second half
        while rev:
            temp = rev.next
            rev.next = right
            right = rev
            rev = temp
        
        # prev points to the head of right
        while left and right:
            after = left.next
            prev = right.next
            left.next = right
            left = after
            right.next = left
            right = prev
        
        
        

        

        
        # we reverse the list first, storing it into another linked list

        # must reverse the last half of the list

        # the issue is we want n - 1 