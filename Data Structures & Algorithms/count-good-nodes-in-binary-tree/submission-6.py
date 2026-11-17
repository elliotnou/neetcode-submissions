# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # the height calculator shud carry a max val

        good = 0
        def height(root, maxVal):
            nonlocal good
            if not root:
                return 0
            
            if root.val >= maxVal:
                good += 1
                maxVal = root.val
            
            return 1 + max(height(root.left, maxVal), height(root.right, maxVal))
            
            
        
        height(root, root.val)
        return good

                
            