# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sumlist = ListNode()
        dummy = sumlist

        carry = 0
        while l1 or l2 or carry:
            totsum = carry
            if l1:
                totsum += l1.val
                l1 = l1.next
            if l2:
                totsum += l2.val
                l2 = l2.next
            
            carry = totsum // 10
            sumlist.next = ListNode(totsum % 10, None)
            sumlist = sumlist.next
        
        return dummy.next
