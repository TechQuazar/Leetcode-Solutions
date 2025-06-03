# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recur(node,curr):
            nonlocal res
            if node.left is None and node.right is None:
                # is child
                res+= curr*10 + node.val
                return
            if node.left:
                recur(node.left,curr*10+node.val)
            if node.right:
                recur(node.right,curr*10+node.val)
            return
        recur(root,0)
        return res