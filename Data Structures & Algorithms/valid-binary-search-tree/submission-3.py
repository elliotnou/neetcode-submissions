# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # dfs should carry information about the MIN and MAX of the parents its visited.
        # at every depth, the node on the LEFT has a MINCAP and a MAXCAP
        # to the left, the node must be LESS than the min(parent.val, grandparent.val)
        # to the right, the node must be GREATER than the max(parent.val, grandparent.val)
        def dfs(root, low, high):
            if not root:
                return True

            if not low < root.val < high:
                return False
            
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

        return dfs(root, float("-inf"), float("inf"))
            
        

