# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS

        ret = []
        q = deque([root])
        if not root: return ret
        while q:
            level = []
            for _ in range(len(q)): # snapshots length of q at this level (length of the level)
                
                node = q.popleft() # takes most leftmost node
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # after this for loop, the only nodes are the nodes on the NEXT level
            ret.append(level)
        
        return ret
                

