<h2><a href="https://leetcode.com/problems/linked-list-cycle">141. Linked List Cycle</a></h2><h3>Easy</h3><hr><p>Given <code>head</code>, the head of a linked list, determine if the linked list has a cycle in it.</p>

<p>There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the&nbsp;<code>next</code>&nbsp;pointer. Internally, <code>pos</code>&nbsp;is used to denote the index of the node that&nbsp;tail&#39;s&nbsp;<code>next</code>&nbsp;pointer is connected to.&nbsp;<strong>Note that&nbsp;<code>pos</code>&nbsp;is not passed as a parameter</strong>.</p>

<p>Return&nbsp;<code>true</code><em> if there is a cycle in the linked list</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 300px; height: 97px; margin-top: 8px; margin-bottom: 8px;" />
<pre>
<strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="width: 141px; height: 74px;" />
<pre>
<strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 0th node.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="width: 45px; height: 45px;" />
<pre>
<strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no cycle in the linked list.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>pos</code> is <code>-1</code> or a <strong>valid index</strong> in the linked-list.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it using <code>O(1)</code> (i.e. constant) memory?</p>

# Solution
Given `head`, the `head` of a linked list, determine if the linked list has a cycle in it.

- There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. J**Note that pos is not passed as a parameter.**

- Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
---

#### Intuition💡:
- Use `two pointers` : `slow (tortoise 🐢 )` and `fast (hare 🐇 )`. **The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there's a cycle, the fast pointer will eventually meet the slow pointer inside the cycle. If there's no cycle, the fast pointer will reach the end of the list.**

1. Floyd’s Cycle-Finding Algorithm // fast slow approach // 2 pointers
2. tortoise and the hare algorithm (Tortoise and Hare)
3. For More Visualization for Beginner (Floyd's Tortoise and Hare Explained)

---
#### Approach
1. Start both pointers at the head of the list.
2. Move `slow` by 1 step and `fast` by 2 step
3.if `fast` meets `slow`, a cycle exists.
4. If `fast` reaches the end(null) no cycle exists. 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
            slow = head
            fast = head

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True  # Cycle detected

            return False  # No cycle
```
