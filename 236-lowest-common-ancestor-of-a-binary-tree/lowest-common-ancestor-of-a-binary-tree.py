# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        LCA if p,q exsists. If not return None
        Find LCA through DFS. 
        1. we search its children recursively, and return the P or Q node if they are found, else return None
        2. We also check if curr is p or q.
        3. We need either (p and q) to be true or we need curr and (p or q) to be true. If both conditions are not, we return None
        for not found.
        TC O(N), N = total nodes, SC O(H), height of tree for recursive stack
        - follow up: How will your function ensure that both p and q were actually found before returning the result?
        we can have 2 variables, foundP and foundQ, which will be set depending on what each recursion returns using if else
        - hint
        return LCA, foundP, foundQ.
        """
        def recur(node):
            if not node:
                return (None, False, False)
            
            leftLCA, leftP, leftQ = recur(node.left)
            rightLCA, rightP, rightQ = recur(node.right)

            currP = node==p
            currQ = node==q
            
            foundP = leftP or rightP or currP
            foundQ = leftQ or rightQ or currQ

            if leftLCA:
                return (leftLCA, foundP, foundQ)
            if rightLCA:
                return (rightLCA, foundP, foundQ)

            if (leftP and rightQ) or (leftQ and rightP) or (currP and (leftQ or rightQ)) or (currQ and (leftP or rightP)):
                return (node, foundP, foundQ)
            
            return (None, foundP, foundQ)

        LCA, foundP, foundQ = recur(root)
        if foundP and foundQ:
            return LCA
        return None
            
            

