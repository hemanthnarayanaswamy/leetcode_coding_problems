# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head and head.val == val:
            head = head.next
    
        if head and head.next:
            prev = head
            curr = head.next

            while curr:
                if curr.val == val:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    prev = curr
                    curr = curr.next
        return head