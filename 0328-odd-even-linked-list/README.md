<h2><a href="https://leetcode.com/problems/odd-even-linked-list">328. Odd Even Linked List</a></h2><h3>Medium</h3><hr><p>Given the <code>head</code> of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return <em>the reordered list</em>.</p>

<p>The <strong>first</strong> node is considered <strong>odd</strong>, and the <strong>second</strong> node is <strong>even</strong>, and so on.</p>

<p>Note that the relative order inside both the even and odd groups should remain as it was in the input.</p>

<p>You must solve the problem&nbsp;in <code>O(1)</code>&nbsp;extra space complexity and <code>O(n)</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg" style="width: 300px; height: 123px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,3,5,2,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [2,1,3,5,6,4,7]
<strong>Output:</strong> [2,3,6,7,1,5,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the linked list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>6</sup> &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
</ul>

# Approach
**"Please note here we are talking about the node number and not the value in the nodes.".**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # Handle short and no LL initially
            return head

        dummyEven = ListNode(0)
        even = dummyEven
        prev = cur = head (The main LL will be odd and we build even and at the end we connect even to main)

        while cur and cur.next:
            nxt = cur.next # we skip the evens and remove them from main and link them to dummy new ll
            even.next = nxt
            even = even.next
            cur.next = nxt.next
            prev = cur 
            cur = cur.next

        even.next = None # We end the even properly
        if cur: # If cur is even we use it or we use the prev
            cur.next = dummyEven.next
        else:
            prev.next = dummyEven.next
        
        return head
```
* Avoid `dummy` allocation; keep `even_head = head.next`
* You can remove `prev` and end-branching if you maintain separate `odd` and `even` runners.
* Repeated rewiring via temporary `next` is extra work; standard two-pointer relink is fewer assignments per look
* Loop condition can be driven by even runner `while even and even.next` for cleaner invariants.
* `odd tail points to saved even head.`
---
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even_head = head.next
        even = even_head

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
```
