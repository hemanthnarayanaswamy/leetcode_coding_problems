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
        
        prev = list1
        cur = list1.next

        node = 1

        while cur:
            if node == a:
                prev.next = list2
            if node == b:
                tail2.next = cur.next
                break
                
            node += 1
            prev = cur
            cur = cur.next
        
        return list1
