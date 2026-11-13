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

        def height(tree):
            if not tree: return 0
            return 1 + max(height(tree.left), height(tree.right))
        
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), height(root.left)+height(root.right))

