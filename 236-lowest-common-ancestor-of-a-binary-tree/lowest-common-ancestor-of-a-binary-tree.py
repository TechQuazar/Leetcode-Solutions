# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        LC interview simul
        1. p,q have a common parent
        2. p contains q
        3. q contains p
        Brute force - given uniq node values, maintain 2 lists that track the path from root to p and q
        find the first common element in both lists from the right to left -> O(N**2) op, where N = total nodes
        -hint
        That works, but can you think of a way to find the LCA without explicitly storing the entire paths? Is there a way to       identify the common ancestor during traversal itself?"
        After hint
        if we DFS, we will reach p/q first. Recursively, we can alert each node that p has been found, and if the same node
        finds q in its other path, its the LCA.
        Approach OK, start coding
        1. each node checks its left and right subtrees.
        2. if p/q is found, it returns True.
        3. The parent catches that true, and passes it along to its right child
        4. How to return the result? The LCA will catch it.
        5. Function declr - node, foundP, foundQ.
        """
        res = None
        def recur(node):
            nonlocal res
            if not node:
                return False
            foundP = recur(node.left)
            foundQ = recur(node.right)
            foundX = node.val==p.val or node.val==q.val
            if ((foundP or foundQ) and foundX) or (not foundX and foundP and foundQ):
                res = node
            return foundP or foundQ or foundX
        recur(root)
        return res
            
