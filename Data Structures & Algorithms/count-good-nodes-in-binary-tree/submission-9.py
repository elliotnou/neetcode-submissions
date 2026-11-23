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

        def dfs(root, maxVal):
            if not root: return 0
            res = 0
            if root.val >= maxVal: res += 1
            maxVal = max(maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            return res
            
        return dfs(root, root.val)