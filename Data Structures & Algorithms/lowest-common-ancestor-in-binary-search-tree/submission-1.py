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

        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

        