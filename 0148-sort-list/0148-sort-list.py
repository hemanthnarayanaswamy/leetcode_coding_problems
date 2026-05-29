# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        arr.sort()

        cur = head
        for num in arr:
            cur.val = num
            cur = cur.next
        
        return head