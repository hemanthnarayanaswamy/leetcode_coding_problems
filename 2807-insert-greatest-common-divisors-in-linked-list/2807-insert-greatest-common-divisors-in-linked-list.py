# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, (a % b)
            return a
        
        cur = head

        while cur and cur.next:
            c = gcd(cur.val, cur.next.val)
            new = ListNode(c)
            new.next = cur.next
            cur.next = new
            cur = cur.next.next
        
        return head