<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list">83. Remove Duplicates from Sorted List</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a sorted linked list, <em>delete all duplicates such that each element appears only once</em>. Return <em>the linked list <strong>sorted</strong> as well</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list1.jpg" style="width: 302px; height: 242px;" />
<pre>
<strong>Input:</strong> head = [1,1,2]
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,1,2,3,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 300]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>The list is guaranteed to be <strong>sorted</strong> in ascending order.</li>
</ul>

# Solution 
1. First, we check if `head or head.next is None`, if it is then we return `None`, It is mandatory to do this check.
2. We use set to store the `unique values` and if any occuring `val` is in the `unique values`, then we shift the pointers. 
3. `prev = head` & we store the `prev.val` in unique initially and `curr = head.next`
4. We use the `while loop` for travesing the linked link and if we find a element that is already in `unique`,
    - we point the `pre.next` to point to `curr.next` as we need to skip `curr` and `curr = curr.next`
    - else, we add the `new val to uniuqe` and `prev = curr` and `curr = curr.next`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = head
        curr = head.next
        unique = {prev.val}

        while curr:
            if curr.val in unique:
                prev.next = curr.next
            else:
                unique.add(curr.val)
                prev = curr

            curr = curr.next
        
        return head
```
---
# Optimal Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
```
