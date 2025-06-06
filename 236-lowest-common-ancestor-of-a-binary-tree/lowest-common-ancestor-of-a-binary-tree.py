# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node):
            if not node:
                return None
            foundP = recur(node.left)
            foundQ = recur(node.right)
            foundX = node if (node.val==p.val or node.val==q.val) else None
            if ((foundP or foundQ) and foundX) or (not foundX and foundP and foundQ):
                return node
            if foundX:
                return foundX
            if foundP:
                return foundP
            return foundQ
        return recur(root)
            
