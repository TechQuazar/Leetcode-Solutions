# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return (0,0) # total sum, number of children in subtree
            
            left, numLeft = dfs(node.left)
            right,numRight = dfs(node.right)
            
            if (left+right+node.val)//(numLeft+numRight+1) == node.val:
                res+=1

            return ((left+right+node.val),numLeft+numRight+1)
            
        dfs(root)
        return res