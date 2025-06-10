# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node):
            nonlocal res
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            res = max(res,left+right+1)
            return max(left,right)+1
        
        recur(root)
        return res-1