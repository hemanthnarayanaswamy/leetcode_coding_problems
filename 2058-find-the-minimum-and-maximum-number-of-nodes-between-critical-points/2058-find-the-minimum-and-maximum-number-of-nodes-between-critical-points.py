# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        n = 1
        nodes = []
        prev = head
        cur = head.next

        while cur.next:
            nxt = cur.next
            if (prev.val > cur.val < nxt.val) or (prev.val < cur.val > nxt.val) :
                nodes.append(n)
            n += 1
            prev = cur
            cur = nxt
        
        if len(nodes) < 2:
            return [-1, -1]
        
        minDist = float('inf')
        maxDist = nodes[-1] - nodes[0]

        for i in range(1, len(nodes)):
            minDist = min(minDist, nodes[i]-nodes[i-1])
            if minDist == 1:
                break
            
        return [minDist, maxDist]