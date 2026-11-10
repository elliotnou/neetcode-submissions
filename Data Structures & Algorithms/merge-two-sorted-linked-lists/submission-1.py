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
        while cur1 or cur2:
            if not cur1:
                merged.next = cur2
                cur2 = cur2.next
            elif not cur2:
                merged.next = cur1
                cur1 = cur1.next
            elif cur2.val <= cur1.val:
                merged.next = cur2
                cur2 = cur2.next
            else:
                merged.next = cur1
                cur1 = cur1.next

            merged = merged.next
        
        return head.next
                
