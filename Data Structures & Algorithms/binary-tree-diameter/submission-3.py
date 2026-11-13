# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at every level, the diameter is the max(curmax, height of left+height of right)
        if not root:
            return 0
            
        best = 0
        def height(tree):
            nonlocal best
            if not tree: return 0
            best = max(best, height(tree.left) + height(tree.right))
            return 1 + max(height(tree.left), height(tree.right))
        
        height(root)
        return best
 
