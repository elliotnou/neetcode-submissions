# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # for a given node, its descendents are itself, everything to the left, and everything to the right
        # perhaps at every node we run binary search on left and right to see if it can find both p and q -- 
        # how do we know this is lowest? if the p and q are on DIFFERENT sides of the node, it is the lowest -- if theyre both on the left, search left. if theyre both on right, search right
        # if the node EQUALS either p or q, it MUST be the lowest. return.

        if root == p or root == q:
            return root
        if self.search(root.left, p) and self.search(root.right, q) or self.search(root.right, p) and self.search(root.left, q):
            return root
        if self.search(root.left, p) and not self.search(root.right, q) or self.search(root.left, q) and not self.search(root.right, p):
            return self.lowestCommonAncestor(root.left, p, q)
        if self.search(root.right, p) and not self.search(root.left, q) or search(root.right, q) and not search(root.left, p):
            return self.lowestCommonAncestor(root.right, p, q)
        
    
    def search(self, tree, node):
        if not tree:
            return False
        if tree.val == node.val:
            return True
        if tree.val > node.val:
            return self.search(tree.left, node)
        else:
            return self.search(tree.right, node)
        

        