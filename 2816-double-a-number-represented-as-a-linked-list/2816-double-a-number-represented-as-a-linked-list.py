# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverselinkedlist(h):
            prev = None
            cur = h

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev
        
        head = reverselinkedlist(head)

        cur = head
        carry = 0

        while cur:
            v = (cur.val * 2) + carry
            carry, cur.val = divmod(v, 10)
            cur = cur.next
        
        head = reverselinkedlist(head)

        if carry:
            fullHead = ListNode(carry, head)
            head = fullHead

        return head
        


            



