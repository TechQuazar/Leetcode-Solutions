"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        seen = set()
        curr = Node(node.val)
        res = curr
        q.append((node,curr))
        nodeMap = {}
        nodeMap[node.val] = curr
        while q:
            og, curr = q.popleft()
            for nei in og.neighbors:
                if nei.val not in nodeMap:
                    newNode = Node(nei.val)
                    nodeMap[nei.val] = newNode
                    q.append((nei, nodeMap[nei.val]))
                curr.neighbors.append(nodeMap[nei.val])

        # print('res',res.val, res.neighbors)
        return res