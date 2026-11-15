# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # thinking of recursing, passing a list of all visited node values
        # at every node, if the node.val is greater than max of visited.values(), add one to the good
        # at the end, return like the "good"

        def isGood(root, maxVal):

            if not root: return 0

            if root.val >= maxVal:
                res = 1
                maxVal = root.val
            else:
                res = 0

            res += isGood(root.left, maxVal)
            res += isGood(root.right, maxVal)

            return res
        
        return isGood(root, root.val)

            