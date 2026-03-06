# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        forward = delay = dummy

        for _ in range(n):
            forward = forward.next
        
        while forward.next:
            forward = forward.next
            delay = delay.next
            
        delay.next = delay.next.next

        return dummy.next