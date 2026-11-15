# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # anything on the LAST of the level should be appended to ret
        # that is, when queue is just one node

        if not root:
            return []
        ret = []
        q = deque([root])
        while q:
            qLen = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i == qLen-1:
                    ret.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ret


