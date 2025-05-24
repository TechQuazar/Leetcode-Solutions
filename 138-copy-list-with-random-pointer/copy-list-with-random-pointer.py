"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        - for each node -> make its copy, then assign pointers to proper copies
        - values can be duplicates so we cant use a hashmap to store nodes as per values.
        - we can maybe assign uniq indices outselves
        - we get the node next values, so we can do that

        Assign each node to uniq index. Keep OGMap for ogIdx-> ogNode
        While OG traversal, create new node and track using copyMap ogIdx -> new Node
        Traverse OG again, then fix random pointers
        O(N) time O(N) space
        """
        i = 0
        copyMap = defaultdict(Node)
        rMap = defaultdict(int)
        nodeToIdx = defaultdict(int)
        curr = head
        prev = Node(-1) # dummy
        res = prev
        while curr!=None:
            newNode = Node(curr.val)
            prev.next = newNode
            copyMap[i] = newNode
            nodeToIdx[curr] = i
            prev = newNode
            curr = curr.next
            i+=1
        curr = head
        # nodeToIdx -> og node -> what idx
        # rMap[i] -> idx to which random OG node
        i=0
        while curr!=None:
            rMap[i] = nodeToIdx[curr.random] if curr.random else -1
            curr = curr.next
            i+=1
        curr = res.next
        i = 0

        # assign the random nodes
        while curr!=None:
            curr.random = copyMap[rMap[i]] if rMap[i]!=-1 else None
            curr = curr.next
            i+=1
        return res.next