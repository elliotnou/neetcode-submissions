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
            lenc = 0
            for _ in range(qLen):
                lenc += 1
                node = q.popleft()
                if lenc == qLen:
                    ret.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ret


