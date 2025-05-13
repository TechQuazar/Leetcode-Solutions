# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        for each LL, need to track which node we are at. Can maintain HashMap for that
        O(total nodes => k*(avg nodes))
        '''
        LLidx = defaultdict(ListNode)
        res = ListNode()
        prev = res
        n = len(lists)
        for i in range(n):
            LLidx[i] = lists[i] if lists[i] != None else None
        #print('LLidx',LLidx)
        completed = set()
        while len(completed)<n:
            minVal = float('inf')
            minListIdx = -1
            for i in range(n):
                if LLidx[i]!= None and LLidx[i].val < minVal:
                    minVal = LLidx[i].val
                    minListIdx = i
            if minListIdx==-1:
                return res.next
            currNode = ListNode(minVal)
            LLidx[minListIdx] = LLidx[minListIdx].next
            if LLidx[minListIdx]==None:
                    completed.add(minListIdx)
            prev.next = currNode
            prev = currNode

        return res.next