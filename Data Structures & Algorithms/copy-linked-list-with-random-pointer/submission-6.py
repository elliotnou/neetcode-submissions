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
        # go thru it once, copying the VALUES into the oldtonew

        cur = head
        oldtonew = {None: None}
        while cur:
            oldtonew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            oldtonew[cur].next = oldtonew[cur.next]
            oldtonew[cur].random = oldtonew[cur.random]
            cur = cur.next
        
        return oldtonew[head]
