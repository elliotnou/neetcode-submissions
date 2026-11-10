# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        merged = ListNode()
        head = merged

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                merged.next = cur1
                cur1 = cur1.next
                merged = merged.next
            else:
                merged.next = cur2
                cur2 = cur2.next
                merged = merged.next
        
        if cur1:
            merged.next = cur1
        elif cur2:
            merged.next = cur2
        
        return head.next