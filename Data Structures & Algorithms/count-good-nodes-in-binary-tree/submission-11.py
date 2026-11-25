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


        def dfs(root, maxVal):
            if not root: return 0
            
            if root.val >= maxVal: 
                ret = 1
                maxVal = root.val
            else:
                ret = 0
            
            ret += dfs(root.left, maxVal)
            ret += dfs(root.right, maxVal)
            return ret
        
        return dfs(root, root.val)

