# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a good node is one in which it is greater than or equal to the max val of the nodes its visited

        def dfs(root, maxVal):
            if not root:
                return 0
            
            if root.val >= maxVal:
                ret = 1
                maxVal = root.val
            else:
                ret = 0
            ret += dfs(root.left, maxVal)
            ret += dfs(root.right, maxVal)

            return ret
        
        return dfs(root, root.val)
            

            
            
