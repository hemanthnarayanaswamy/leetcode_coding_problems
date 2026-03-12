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
            nxt = cur.next
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        dummy = ListNode(0)
        cur = dummy 
        for i in range(len(stack)):
            cur.next = stack[i]
            cur = cur.next
        cur.next = None

        return dummy.next
