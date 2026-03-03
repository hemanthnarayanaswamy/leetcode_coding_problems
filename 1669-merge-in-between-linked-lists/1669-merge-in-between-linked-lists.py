# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        
        cur = list1
        node = 1

        while cur:
            next = cur.next
            if node == a:
                cur.next = list2
            if node == b+1:
                tail2.next = cur.next
                break

            node += 1
            cur = next
        
        return list1
