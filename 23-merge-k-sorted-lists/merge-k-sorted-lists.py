# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        PQ
        '''
        pq = []
        for i,node in enumerate(lists):
            if node != None:
                heapq.heappush(pq,(node.val,i,node)) # i because when values are same, we can use idx to compare
        
        res = ListNode()
        prev = res
        while pq:
            val,i, node = heapq.heappop(pq)
            currNode = ListNode(val)
            prev.next = currNode
            prev = currNode
            if node.next!=None:
                heapq.heappush(pq,(node.next.val,i,node.next))

        return res.next