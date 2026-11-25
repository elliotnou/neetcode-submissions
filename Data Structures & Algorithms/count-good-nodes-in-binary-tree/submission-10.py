# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # need a counter; every node has the potential to be good, everything must be visited
        # dfs, which tracks and passes down the current max node visited in that path

        count = 0

        def dfs(root, maxVal):
            nonlocal count
            if not root: return
            
            if root.val >= maxVal: 
                count += 1
                maxVal = root.val
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
            return
        
        dfs(root, root.val)
        return count

