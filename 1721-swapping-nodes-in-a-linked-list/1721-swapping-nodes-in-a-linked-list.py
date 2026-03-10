# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head

        for i in range(k):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        cur = head
        n = 1
        while n != k:
            cur = cur.next
            n += 1
        
        slow.val, cur.val = cur.val, slow.val

        return head