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
        # first pass: we copy all the head nodes to to a new in a dict

        # second pass: we link all the nodes and set their randoms

        oldtonew = {None: None}

        cur = head
        while cur:
            oldtonew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            oldtonew[cur].next = oldtonew[cur.next]
            oldtonew[cur].random = oldtonew[cur.random]
            cur = cur.next
        
        return oldtonew[head]