# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        def recur(curr, x):
            if curr==None:
                return None
            node = TreeNode(x)
            left = recur(curr.left,2*x+1)
            right = recur(curr.right,2*x+2)
            node.left = left
            node.right = right
            return node
        self.root = recur(root,0)

        

    def find(self, target: int) -> bool:
        
        def recur(node):
            if node==None:
                return False
            if node.val == target:
                return True
            return recur(node.left) or recur(node.right)
        
        return recur(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)