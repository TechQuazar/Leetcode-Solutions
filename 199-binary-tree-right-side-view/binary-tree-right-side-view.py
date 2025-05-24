# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS, keep track of each level; have you filled the val for that level?
        """

        res = []
        if not root:
            return res
        q = deque()
        q.append((root,0)) # node,level
        levelFilled = defaultdict(bool)
        while q:
            node, level = q.popleft()
            if level not in levelFilled:
                res.append(node.val)
                levelFilled[level] = True
            if node.right:
                q.append((node.right,level+1))
            if node.left:
                q.append((node.left,level+1))

        return res