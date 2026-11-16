# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # we maintain a left and right range
        # if something is to the RIGHT
        #   check that its GREATER than parent but less than right range
        #   update left range to parent.val
        # if something is tot he left
        #   check that its smaller than the parent but greater than left range
        #   update right range to parent.val

        def validate(root, left, right):
            if not root:
                return True
            
            if not left < root.val < right:
                return False
            
            return validate(root.left, left, min(right, root.val)) and validate(root.right, max(left, root.val), right)
        
        return validate(root, float("-inf"), float("inf"))
