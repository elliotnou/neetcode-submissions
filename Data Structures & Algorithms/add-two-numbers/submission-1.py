# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # l1.val + l2.val % 10 is carried over to the next calculation
        # if l1 is None, 0. if. l2 is None, 0. if they are both None, finish but create a node if any carried over

        sumlist = ListNode(0, None)
        ret = sumlist
        carry = 0

        totsum = 0
        while l1 or l2:
            if not l1:
                totsum = l2.val + carry
                l2 = l2.next
            elif not l2:
                totsum = l1.val + carry
                l1 = l1.next
            else:
                totsum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            sumlist.next = ListNode(totsum % 10, None)
            if totsum >= 10:
                    carry = 1
            else:
                    carry = 0

            sumlist = sumlist.next
            
        
        if carry == 1:
            sumlist.next = ListNode(1, None)
        
        return ret.next


