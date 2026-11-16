# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # use a deque
        # the last node to be processed in a level is the RIGHT SIDE VIEW
        # however, we must ensure that nullnodes are never added to the queue so they are not mistaken as a right side node

        ret = []
        q = deque([root])
        if not root:
            return ret
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if i == qLen - 1:
                    ret.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ret
