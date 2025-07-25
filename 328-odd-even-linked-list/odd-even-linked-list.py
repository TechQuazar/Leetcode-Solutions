# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        first = head
        second = head.next
        oddIdx = True
        curr = second.next
        l = first # last odd node
        r = second # last even node
        while curr:
            if oddIdx:
                l.next = curr
                nextNode = curr.next
                curr.next = second
                r.next = nextNode
                l = l.next
                oddIdx = False
                curr = nextNode
            else:
                r = r.next
                oddIdx = True
                curr = r.next
        
        return first