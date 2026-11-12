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

        cur = head
        while cur:
            copy = Node(cur.val) # copy the heads val
            oldtonew[cur] = copy # key is head node val is copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtonew[cur]
            copy.next = oldtonew[cur.next]
            copy.random = oldtonew[cur.random]
            cur = cur.next

        return oldtonew[head]

