# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        carry = 0
        sumlist = ListNode()
        dummy = sumlist
        while carry or cur1 or cur2:
            value = carry
            if cur1:
                value += cur1.val
                cur1 = cur1.next
            if cur2:
                value += cur2.val
                cur2 = cur2.next
            
            node = ListNode(value % 10)
            carry = value // 10
            sumlist.next = node
            sumlist = sumlist.next
        
        return dummy.next
