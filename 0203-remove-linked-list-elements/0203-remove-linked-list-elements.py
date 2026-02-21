class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0, head)   # Dummy node pointing to head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next   # Remove node
            else:
                current = current.next

        return dummy.next