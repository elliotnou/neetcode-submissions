# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs

        q = deque([root])
        ret = []
        if not root:
            return ret


        while q:
            qLen = len(q)
            for i in range(len(q)): #snapshots that length
                node = q.popleft()
                if i == qLen - 1:
                    ret.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ret
