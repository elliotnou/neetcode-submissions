# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder in a BST comes out sorted
        # so,o the kth is the kth int he sorted in order traversal
        
        val = []
        def inorder(node):
            nonlocal val
            if not node:
                return
            
            inorder(node.left)
            val.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return val[k-1]
