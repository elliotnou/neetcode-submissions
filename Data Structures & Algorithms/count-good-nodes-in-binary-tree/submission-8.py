# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # do a dfs, which carries the max of the value of the nodes its visited thus far.
        # if the current node in the dfs is greater than or equal to the max, it's considered a good node

        count = 0
        def dfs(root, maxVal):
            nonlocal count
            if not root: return
            if root.val >= maxVal:
                count += 1
            dfs(root.left, max(maxVal, root.val))
            dfs(root.right, max(maxVal, root.val))
            return
        dfs(root, root.val)
        return count