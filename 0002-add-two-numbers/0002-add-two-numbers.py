# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(a, b, c):
            res = a+b+c
            n = res % 10
            car = res // 10
            return n, car
        
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            n, carry = add(a, b, carry)
                
            cur.next = ListNode(n)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        cur.next = None

        return dummy.next
            