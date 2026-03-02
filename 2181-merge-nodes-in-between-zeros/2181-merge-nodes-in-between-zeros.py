# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zeroPointer = head
        nonZeroPointer = head.next

        while nonZeroPointer and nonZeroPointer.next:
            c, v, n = nonZeroPointer, nonZeroPointer.val, nonZeroPointer.next
            if v != 0:
                zeroPointer.val += v
            else:
                zeroPointer.next = c
                zeroPointer = zeroPointer.next      
            nonZeroPointer = n
        
        zeroPointer.next = None
        return head
