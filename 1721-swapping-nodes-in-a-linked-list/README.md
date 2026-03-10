<h2><a href="https://leetcode.com/problems/swapping-nodes-in-a-linked-list">528. Swapping Nodes in a Linked List</a></h2><h3>Medium</h3><hr><p>You are given the <code>head</code> of a linked list, and an integer <code>k</code>.</p>

<p>Return <em>the head of the linked list after <strong>swapping</strong> the values of the </em><code>k<sup>th</sup></code> <em>node from the beginning and the </em><code>k<sup>th</sup></code> <em>node from the end (the list is <strong>1-indexed</strong>).</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg" style="width: 400px; height: 112px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [1,4,3,2,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [7,9,6,6,7,8,3,0,9,5], k = 5
<strong>Output:</strong> [7,9,6,6,8,7,3,0,9,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>

---

## Approach 
1. We first use the, `fast & slow` pointer techniques to find the kth node from the last and save it's position.
2. And in the next iteration take `cur` pointer to the kth node from the start. 
3. Once we have two positions locked-in, we swap there values `slow.val, cur.val = cur.val, slow.val` and return `head`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head

        for i in range(k):
            fast = fast.next
        
        cur = fast
        while fast:
            slow = slow.next
            fast = fast.next
        
        cur = head
        n = 1
        while n != k:
            cur = cur.next
            n += 1
        
        slow.val, cur.val = cur.val, slow.val

        return head
```

* We'll try to combine everything under one iteration.
* We are already moving the fast pointer by kth nodes, which means its already passed the kth node from start so we assign current when fast is at kth node to avoid, double iteration. 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head

        for i in range(k-1):
            cur = cur.next
        
        fast = cur.next
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.val, cur.val = cur.val, slow.val

        return head
```
