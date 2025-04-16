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
        q.append(node)
        curr = Node(node.val)
        res = curr
        nodeMap = {}
        nodeMap[node.val] = curr
        while q:
            og = q.popleft()
            for nei in og.neighbors:
                if nei.val not in nodeMap:
                    newNode = Node(nei.val)
                    nodeMap[nei.val] = newNode
                    q.append(nei)
                nodeMap[og.val].neighbors.append(nodeMap[nei.val])

        # print('res',res.val, res.neighbors)
        return res