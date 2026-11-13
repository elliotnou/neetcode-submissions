# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(depth, treenode):
            if not treenode: return depth

            return max(traverse(depth+1, treenode.left), traverse(depth+1, treenode.right))
        
        return traverse(0, root)