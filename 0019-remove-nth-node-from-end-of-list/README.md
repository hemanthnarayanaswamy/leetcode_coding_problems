<h2><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list">19. Remove Nth Node From End of List</a></h2><h3>Medium</h3><hr><p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do this in one pass?</p>

# Fast & Slow Pointer Approach
**MY ONLY MISTAKE WAS NOT CONSIDERING THE DUMMY POINTER**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward = delay = head

        while n:
            forward = forward.next
            n -= 1
        
        if not forward: # Here we can return NONE, but if n == lenght, then also forward will be none, but we need to remove the first node, 
            return head.next # so we remove head and return head.next (which will still be none)
        
        while forward.next:
            forward = forward.next
            delay = delay.next
            
        delay.next = delay.next.next

        return head
```
---
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        forward = delay = dummy

        for _ in range(n):
            forward = forward.next
        
        while forward.next:
            forward = forward.next
            delay = delay.next
            
        delay.next = delay.next.next

        return dummy.next
```
* Here we initiated a `dummy` node and start the pointers `slow & fast` at dummy, and we fast forward `fast` pointer to `slow + n` positions forward. 
* now until `fast.next` we move and now when we find the end of iteration. 
* The since the distance between `slow & fast` was `n`, when the `fast` is at the end `slow` should be at `end - n`, that means we need to delete the next node from the slow. 
* so `slow.next = slow.next.next` skip the next node. 
* return `dummy.next` i.e `head`.
