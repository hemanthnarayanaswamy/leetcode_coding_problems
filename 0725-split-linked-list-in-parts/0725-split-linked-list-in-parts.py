# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        res = []

        while cur:
            cur = cur.next
            n += 1
        
        d, r = divmod(n, k)

        cur = head

        while k:
            dummy = ListNode(0)
            new = dummy
            if r:
                split = d + 1
                r -= 1
            else:
                split = d

            while split:
                dummy.next = cur
                dummy = dummy.next
                cur = cur.next
                split -= 1
            
            dummy.next = None
            res.append(new.next)
            k -= 1
        
        return res


