<h2><a href="https://leetcode.com/problems/rotate-list">61. Rotate List</a></h2><h3>Medium</h3><hr><p>Given the <code>head</code> of a linked&nbsp;list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px; height: 191px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 305px; height: 350px;" />
<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>

# Approach
![img](https://th.bing.com/th/id/OIP.cNVOvSJcsnjHSs18JAUtWQHaEK?w=290&h=180&c=7&r=0&o=7&pid=1.7&rm=3)
* Rotating a linked list involves shifting its nodes to the left or right by a given number of positions.
* First we'll handle some edge cases where  there is no `head` or `k==0`, we return `head`

1. First thing is to make the Linked List circular and for this we need to connect tail to the head and also need to count the nodes.
2. `k = k % n`, sometimes `k > n`, its better this way and if `k%n` then no need to rotation because after `k` rotation, linked list will return to its original. 
3. Make checking this, we start a new iteration and the goal of this iteration is to reach the `new tail` and then make the `head = new tail.next` and `new tail.next = None` to make it non circular again.

```ini
r = k % n.

If r == 0, new tail is the original tail (no rotation).

Otherwise, Starting from head, move n - r - 1 steps; that node is the new tail
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head and k:
            cur = head
            n = 1
        else:
            return head

        while cur.next:
            n += 1
            cur = cur.next

        if (k % n) == 0:
            return head
        else:
            cur.next = head
            cur = cur.next

        skip = n - (k%n) - 1
        while skip:
            cur = cur.next
            skip -= 1
        
        head = cur.next
        cur.next = None

        return head
```
---
```ini
Let’s say k = 2. That means we rotate the list to the right two times. So the new head will be the node that’s 2nd from the end. If k = 3, the new head will be the 3rd from the end, and so on.

There’s a really simple formula to find that spot:

length of the list - k
But here’s the trick — in the actual code, we don’t want to stop at the new head. We want to stop right before it. Why? Because we need to cut the list there, and since it’s a singly linked list, we can’t go backward from the new head. We can only go forward.

So instead, we stop at:

length - k - 1
and then break the link after that node.
```
---
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        # find length
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k %= length
        
        if k == 0:
            return head
        
        # make circular
        tail.next = head
        
        # find new tail
        steps = length - k
        new_tail = head
        
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
```
