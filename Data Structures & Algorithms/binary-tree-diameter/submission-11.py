# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        # at any point, the diameter is the HEIGHT of the left PLUS the height of the right 

        def height(root):
            nonlocal diameter
            if not root: return 0

            d = height(root.left) + height(root.right)
            diameter = max(d, diameter)

            return 1 + max(height(root.left), height(root.right))
        
        height(root)
        return diameter