# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            prev = head
            curr = head.next
            unique = {prev.val}
        else:
            return head

        while curr:
            if curr.val in unique:
                prev.next = curr.next
            else:
                unique.add(curr.val)
                prev = curr

            curr = curr.next
        
        return head

