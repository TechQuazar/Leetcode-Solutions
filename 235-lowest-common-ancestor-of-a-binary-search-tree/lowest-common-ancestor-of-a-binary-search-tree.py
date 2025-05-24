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
        res = None
        def recur(node):
            nonlocal res
            if not node: 
                return
            
            if node.val!= p.val and node.val!=q.val:
                if (p.val< node.val <q.val) or (q.val < node.val < p.val):
                    res = node
                    return
                else:
                    if p.val < node.val and q.val < node.val:
                        recur(node.left)
                    elif p.val> node.val and q.val> node.val:
                        recur(node.right)
            else:
                res = node
            
            return

        recur(root)
        return res