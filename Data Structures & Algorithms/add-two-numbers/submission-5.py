# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # cases to handle: carried 1, one number is longer than the other

        # start adding from leftmost node. at every stage, consider the carry/save the new carry
        # when one list is empty, treat it as a 0
        carry = 0
        sumnode = ListNode()
        dummy = sumnode
        while l1 or l2 or carry:
            totsum = carry
            if l1:
                totsum += l1.val
                l1 = l1.next
            if l2:
                totsum += l2.val
                l2 = l2.next
        
            sumnode.next = ListNode(totsum % 10)
            carry = totsum // 10
            sumnode = sumnode.next

        return dummy.next

