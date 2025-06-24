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
                return (0,True)
            left, isLeftValid = recur(node.left)
            right, isRightValid = recur(node.right)
            if isLeftValid and isRightValid and abs(left-right)<=1:
                return (max(left,right)+1, True)
            
            return (0, False)
        
        return recur(root)[1]
        