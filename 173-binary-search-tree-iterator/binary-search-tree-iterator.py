# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.curr = -1
        self.arr = []
        def recur(node):
            if not node:
                return
            recur(node.left)
            self.arr.append(node.val)
            recur(node.right)
            return
        recur(root)
        self.n = len(self.arr)

    def next(self) -> int:
        self.curr+=1
        return self.arr[self.curr]

    def hasNext(self) -> bool:
        return self.curr+1<self.n


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()