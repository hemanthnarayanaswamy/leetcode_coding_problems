# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p1 = head
            p2 = head.next
        else:
            return head

        while p2:
            p1.val, p2.val = p2.val, p1.val
            
            if p2.next:
                p1 = p2.next
                p2 = p1.next
            else:
                return head
        
        return head