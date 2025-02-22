# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        ''' construct a tree
        1. preorder -> V L R
        2. traversal[0] -> root, then [... end of left side][...end of right side]
        3. D-> will tell us where we are
        4. if curr D == par D+1 and curr->next D == par D+1 => curr, curr.next as sibl
        5. if curr D==par D + 1 and next D < curr D, it means we go up the tree. Then for the curr node, we say its children are both None and return the node

        1 (0) -> 2 (1) -> (lchild) ->

        each node should also return its # of children, so that we can skip #+1 for each curr to see if it has a right child
        '''
        arr = []
        num = ''
        i=0
        while i<len(traversal) and traversal[i]!='-':
            num+=traversal[i]
            i+=1
        arr.append((num,0))
        while i<len(traversal):
            count = 0
            while i!=0 and i<len(traversal) and traversal[i]=='-':
                i+=1
                count+=1
            num = ''
            while i<len(traversal) and traversal[i]!='-':
                num+=traversal[i]
                i+=1
            arr.append((num,count))

        # print(arr)
        n = len(arr)
        def recur(i):
            if i>=n:
                return (None,0)
            val,depth = arr[i]
            val= int(val)
            curr = TreeNode(val)
            nextIdx = i+1
            left,leftChildren = None,0
            right,rightChildren = None,0
            # curr depth==prev depth, left child conf
            if nextIdx<n and depth+1==arr[nextIdx][1]: 
                left,leftChildren = recur(i+1)

            # right child exsists
            rightIdx = i+leftChildren+1
            if  rightIdx<n and depth+1 == arr[rightIdx][1]:
                right,rightChildren = recur(rightIdx)

            curr.left = left
            curr.right = right

            return (curr,1+leftChildren + rightChildren)

        root,_ = recur(0)
        return root
            
        