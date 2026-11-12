"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pass once and deep copy the values
        # during this pass, create a dict where key is the head node and val is the corresponding copy node that was created

        # do a second pass, matchign the randoms

        oldtonew = {None: None}

        dummy = Node(0)
        new = dummy
        while head:
            new.next = Node(head.val, None, head.random)
            new = new.next
            oldtonew[head] = new
            head = head.next
        
        new = dummy
        while new:
            new.random = oldtonew[new.random]
            new = new.next
        
        return dummy.next


