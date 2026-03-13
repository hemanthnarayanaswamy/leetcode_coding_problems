# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(a, b, c):
            res = a+b+c
            if res >= 10:
                n = res % 10
                c = res // 10
            else:
                n = res
                c = 0
            return n, c
        
        dummy = ListNode(0)
        cur = dummy
        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2:
            if p1 and p2:
                n, c = add(p1.val, p2.val, carry)
                p1 = p1.next
                p2 = p2.next
            elif p1 and not p2:
                n, c = add(p1.val, 0, carry)
                p1 = p1.next
            else:
                n, c = add(0, p2.val, carry)
                p2 = p2.next
            
            cur.next = ListNode(n)
            carry = c
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)
            cur = cur.next
        cur.next = None

        return dummy.next
            