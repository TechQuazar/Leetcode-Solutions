# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        prev = res
        carry = 0
        while l1!=None or l2!=None:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            currNode = ListNode((v1+v2+carry)%10)
            carry = (v1+v2+carry)//10
            prev.next = currNode
            prev = currNode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            currNode = ListNode(carry)
            prev.next = currNode

        return res.next
