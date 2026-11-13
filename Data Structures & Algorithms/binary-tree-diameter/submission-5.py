# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(node):
            nonlocal best

            if not node: return 0
            best = max(best, height(node.left) + height(node.right))
            return 1 + max(height(node.left), height(node.right))
        
        height(root)
        return best
 
