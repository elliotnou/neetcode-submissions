# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        def height(root):
            nonlocal maxVal
            if not root: return 0

            l, r = height(root.left), height(root.right)
            maxVal = max(maxVal, l + r)

            
            return 1 + max(l, r)
        height(root)
        return maxVal

