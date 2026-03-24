# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummyEven = ListNode(0)
        even = dummyEven
        prev = cur = head

        while cur and cur.next:
            nxt = cur.next
            even.next = nxt
            even = even.next
            cur.next = nxt.next
            prev = cur
            cur = cur.next

        even.next = None
        if cur:
            cur.next = dummyEven.next
        else:
            prev.next = dummyEven.next
        
        return head