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
        # pass1 -- deep copy, save this node as the VALUE to the key of its index

        # pass2 -- run through copied list, setting the random
        oldtonew = {None: None}


        cur = head
        while cur:
            oldtonew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtonew[cur]
            copy.next = oldtonew[cur.next]
            copy.random = oldtonew[cur.random]
            cur = cur.next
        
        return oldtonew[head]

        