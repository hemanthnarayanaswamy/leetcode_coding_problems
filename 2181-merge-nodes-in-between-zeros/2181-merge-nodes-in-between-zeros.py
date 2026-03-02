# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zeroPointer = head
        nonZeroPointer = head.next
        currentSum = 0

        while nonZeroPointer and nonZeroPointer.next:
            c, v, n = nonZeroPointer, nonZeroPointer.val, nonZeroPointer.next
            if v != 0:
                currentSum += v
            else:
                zeroPointer.val = currentSum
                currentSum = 0
                zeroPointer.next = c
                zeroPointer = zeroPointer.next      
            nonZeroPointer = n
        
        zeroPointer.val = currentSum
        zeroPointer.next = None
        return head
