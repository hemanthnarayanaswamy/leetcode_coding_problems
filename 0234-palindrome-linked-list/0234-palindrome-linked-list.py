# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1. Find the middle using slow & fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. If odd length, skip the middle element
        if fast:
            slow = slow.next

        # 3. Reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # 4. Compare first half and reversed second half
        left, right = head, prev
        while right and left:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True