# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def recur(node,isLeft,depth):
            if not node:
                return depth
            if isLeft:
                depth = max(depth, recur(node.right,False,depth+1), recur(node.left, True, 0))
            else:
                depth = max(depth, recur(node.left,True,depth+1), recur(node.right, False, 0))
            return depth
        
        return max(recur(root.left, True, 0), recur(root.right, False, 0))