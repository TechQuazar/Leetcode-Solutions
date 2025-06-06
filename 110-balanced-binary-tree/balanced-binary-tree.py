# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(node):
            if not node:
                return [True,0]
            leftBal,leftDepth = recur(node.left)
            rightBal,rightDepth = recur(node.right)
            if leftBal and rightBal and abs(leftDepth - rightDepth)<=1:
                return [True, 1 + max(leftDepth, rightDepth)]
            return [False,0]
        return True if recur(root)[0] else False