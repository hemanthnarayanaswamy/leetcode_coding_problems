# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            new_node = math.gcd(prev.val, cur.val)
            new = ListNode(new_node)
            prev.next = new
            new.next = cur
            prev = cur
            cur = cur.next
        return head 