# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        pre -> VLR
        post -> LRV
        root = pre[0]
        leftmost = post[0]
        so u can assume that the node next to root is the left (it can be either left or right, but its fine to assume left)
        lookup that idx in post, all those to left of that idx should be left subtree, similar for right

        '''
        indices = {}
        for i,v in enumerate(postorder):
            indices[v]=i
        i1,i2 = 0,len(preorder)
        j1,j2 = 0,len(postorder)
        
        def recur(i1,i2,j1,j2):
            if i1>i2 or j1>j2:
                return None
            curr = TreeNode(preorder[i1])
            left,right = None, None
            if i1!=i2:
                idx = indices[preorder[i1+1]] # next val
                sizeLeft = idx-j1+1
                sizeRight = i2 - (i1+sizeLeft)
                if sizeLeft>0: 
                    # left can be formed
                    left = recur(i1+1,i1+sizeLeft,j1,j1+sizeLeft-1)
                
                if sizeRight>0:
                    right = recur(i1+sizeLeft+1, i2, j1+sizeLeft,j1+sizeLeft+sizeRight-1)

            curr.left = left
            curr.right = right
            return curr
        return recur(0,len(preorder)-1,0,len(postorder)-1)

        