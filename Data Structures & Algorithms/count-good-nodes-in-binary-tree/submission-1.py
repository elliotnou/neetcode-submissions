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

        good = 0
        maxvisited = root.val
        def isGood(root):
            nonlocal good
            nonlocal maxvisited
            if not root:
                return
            if root.val >= maxvisited:
                good += 1
                maxvisited = root.val
            
            temp = maxvisited
            isGood(root.left)
            maxvisited = temp

            temp = maxvisited
            isGood(root.right)
            maxvisited = temp
            return
        
        isGood(root)
        return good

            