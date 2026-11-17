# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q are on DIFFERENT sides of a node, it is the lowest

        # or if its equal

        # that is, if the value is BETWEEN p and q.

        best = None

        def dfs(root, p, q):
            nonlocal best
            if not root: return
            if p.val < root.val and q.val < root.val:
                dfs(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                dfs(root.right, p, q)
            else:
                best = root
                return 
            

        dfs(root, p, q)
        return best


