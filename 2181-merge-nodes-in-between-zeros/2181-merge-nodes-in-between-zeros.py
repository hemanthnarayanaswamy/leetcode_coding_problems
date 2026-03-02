# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zeroPointer = head
        nonZeroPointer = head.next

        while nonZeroPointer:
            if nonZeroPointer.val != 0:
                zeroPointer.val += nonZeroPointer.val
            else:
                if nonZeroPointer.next:
                    zeroPointer.next = nonZeroPointer
                    zeroPointer = zeroPointer.next 
                else:
                    zeroPointer.next = None
                    return head
                
            nonZeroPointer = nonZeroPointer.next