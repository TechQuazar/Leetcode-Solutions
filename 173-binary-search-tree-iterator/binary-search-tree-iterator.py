# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.push_left(root)
    
    def push_left(self,node):
        while node:
            self.st.append(node)
            node = node.left

    def next(self) -> int:
        top = self.st.pop()
        if top.right:
            self.push_left(top.right)
        return top.val

    def hasNext(self) -> bool:
        return bool(self.st)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()