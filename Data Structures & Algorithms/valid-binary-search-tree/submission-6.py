# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to use a left and right limit to keep track of the allowed
        # if a node goes to the LEFT, the max right range is set to min(right, root.val)

        def dfs(root, left, right):
            if not root:
                return True
            if not left < root.val < right:
                return False
            
            return dfs(root.left, left, min(right, root.val)) and dfs(root.right, max(left, root.val), right)
        

        return dfs(root, float("-inf"), float("inf"))