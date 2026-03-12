# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()

            if stack:
                stack[-1].next = cur
            stack.append(cur)

            cur = cur.next
            stack[-1].next = None

        return stack[0]