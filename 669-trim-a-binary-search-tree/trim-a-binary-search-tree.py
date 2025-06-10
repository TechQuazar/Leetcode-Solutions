# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def recur(node):
            if not node:
                return None
            val = node.val
            if val<low:
                return recur(node.right)
            if val>high:
                return recur(node.left)
            node.left = recur(node.left)
            node.right = recur(node.right)
            return node
        
        return recur(root)