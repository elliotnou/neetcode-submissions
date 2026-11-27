# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # every node must be searched
        # dfs where the information of the largest value visited is carried

        def dfs(root, maxVal):
            if not root: return 0
            
            if root.val >= maxVal:
                res = 1 
                maxVal = root.val
            else:
                res = 0
            
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            return res
        
        return dfs(root, root.val)
        


