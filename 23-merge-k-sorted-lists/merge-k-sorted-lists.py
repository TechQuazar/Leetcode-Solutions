# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i,node in enumerate(lists):
            if node!=None:
                heapq.heappush(pq, (node.val,i,node))

        root = ListNode()
        prev = root
        while pq:
            val,idx,currNode = heapq.heappop(pq)
            newNode = ListNode(val)
            prev.next = newNode
            prev = newNode
            if currNode.next!=None:
                heapq.heappush(pq, (currNode.next.val, idx, currNode.next))
        return root.next