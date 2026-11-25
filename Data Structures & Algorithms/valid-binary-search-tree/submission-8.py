# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we do a dfs and send the left bound and the right bound
        # anything node to the LEFT has an UPPER bound of its parent
        # anything node to the RIGHT has a LOWER bound of its parent

        def dfs(root, lower, upper):

            if not root: return True
            if root.val <= lower or root.val >= upper:
                return False

            return dfs(root.left, lower, min(upper, root.val)) and dfs(root.right, max(lower, root.val), upper)
        
        return dfs(root, float('-inf'), float('inf'))
        