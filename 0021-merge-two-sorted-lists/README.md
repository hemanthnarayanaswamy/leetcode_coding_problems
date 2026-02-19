<h2><a href="https://leetcode.com/problems/merge-two-sorted-lists">21. Merge Two Sorted Lists</a></h2><h3>Easy</h3><hr><p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>

<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>Return <em>the head of the merged linked list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>Input:</strong> list1 = [1,2,4], list2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>Both <code>list1</code> and <code>list2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>

# Merge Two Sorted Lists
* You are given the heads of two sorted linked lists `list1` and `list2`. 
* Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. 
* Return the head of the merged linked list. 


### Approach
** We use `Two Pointer` and `Dummy Node` on linked lists.**
* Since both lists are already sorted, at each step we only need to compare current nodes and pick the smaller one.
* A `dummy` node helps build the result list easily without special handling for the first node.

#### How it Works
    1. Create `dummy` and set `curr=dummy`
    2. While both lists are non-empty:
        * compare `list1.val` and `list2.val`
        * attach the smaller node to `curr.next = list1 or list2`
        * Move that list pointer forward
        * Move `curr` forward
    3. After loop, one list may still have nodes left.
        * Attach the remaining part directly: `curr.next = list1 if list1 else list2`
    4. Return `dummy.next`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        curr.next = list1 if list1 else list2
        
        return dummy.next
```
