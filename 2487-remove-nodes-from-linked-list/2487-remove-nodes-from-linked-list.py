# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(head):
            cur = head
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        

        head = reverseLinkedList(head)
        cur = head
        nxt = cur.next
        while nxt:
            if cur.val > nxt.val:
                cur.next = nxt.next 
            else:
                cur = nxt
            nxt = nxt.next
        
        return reverseLinkedList(head)
        