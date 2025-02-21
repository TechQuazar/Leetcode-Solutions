# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.seen = set()

        def recur(curr, x):
            if curr==None:
                return None
            node = TreeNode(x)
            if x not in self.seen:
                self.seen.add(x)
            left = recur(curr.left,2*x+1)
            right = recur(curr.right,2*x+2)
            node.left = left
            node.right = right
            return node
        self.root = recur(root,0)

        

    def find(self, target: int) -> bool:
        return True if target in self.seen else False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)