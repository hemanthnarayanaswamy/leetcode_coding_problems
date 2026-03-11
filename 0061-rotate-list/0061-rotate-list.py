# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head and k:
            cur = head
            n = 1
        else:
            return head

        while cur.next:
            n += 1
            cur = cur.next

        if (k % n) == 0:
            return head
        else:
            cur.next = head

        skip = n - (k%n) - 1
        pointer = head
        while skip:
            pointer = pointer.next
            skip -= 1
        
        head = pointer.next
        pointer.next = None

        return head
