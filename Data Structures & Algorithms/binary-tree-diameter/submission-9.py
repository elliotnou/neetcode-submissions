# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at any point, the height of left plus the height of right

        maxval = 0

        def height(root):
            nonlocal maxval
            if not root: return 0
            maxval = max(maxval, height(root.left)+height(root.right))
            return 1 + max(height(root.left), height(root.right))
            
        
        height(root)
        return maxval