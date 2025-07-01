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
        newRoot = None
        cache = {}
        q = deque()
        q.append(node)
        while q:
            currNode = q.popleft()
            if not newRoot:
                newRoot = Node(currNode.val)
                cache[currNode.val] = newRoot
            for nei in currNode.neighbors:
                if nei.val not in cache:
                    neiNode = Node(nei.val)
                    cache[nei.val] = neiNode
                    q.append(nei)
                cache[currNode.val].neighbors.append(cache[nei.val])

        return newRoot