# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isbal = True
        
        def height(root):
            nonlocal isbal
            if not root: return 0
            
            l,r = height(root.left), height(root.right)
            if abs(l-r) > 1:
                isbal = False
            
            return 1 + max(l, r)
        
        height(root)
        return isbal

