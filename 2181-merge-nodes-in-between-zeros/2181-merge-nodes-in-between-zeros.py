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
            if nonZeroPointer.val != 0:
                zeroPointer.val += nonZeroPointer.val
            else:
                zeroPointer.next = nonZeroPointer
                zeroPointer = zeroPointer.next      
            nonZeroPointer = nonZeroPointer.next
        
        zeroPointer.next = None
        return head