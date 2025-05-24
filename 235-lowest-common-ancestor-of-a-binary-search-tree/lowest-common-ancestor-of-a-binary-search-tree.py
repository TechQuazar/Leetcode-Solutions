# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        LCA - BST
        as BST, we have root, p, q. Can find if they lie in same subtree or diff based on root val
        If diff, root is LCA
        Recur on curr node. is the value on diff subtree,? if yes return that. If not, recur on its children again.
        I think this is the optimal approach.
        '''
        curr = root
        while curr:
            if p.val<curr.val and q.val<curr.val:
                curr = curr.left
            elif p.val>curr.val and q.val>curr.val:
                curr = curr.right
            else:
                return curr
        