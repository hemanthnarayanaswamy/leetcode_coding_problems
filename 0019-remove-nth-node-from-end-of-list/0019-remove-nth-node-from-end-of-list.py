# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward = delay = head

        while n:
            forward = forward.next
            n -= 1
        
        if not forward:
            return head.next
        
        while forward.next:
            forward = forward.next
            delay = delay.next
            
        delay.next = delay.next.next

        return head