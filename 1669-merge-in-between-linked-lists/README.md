<h2><a href="https://leetcode.com/problems/merge-in-between-linked-lists">1765. Merge In Between Linked Lists</a></h2><h3>Medium</h3><hr><p>You are given two linked lists: <code>list1</code> and <code>list2</code> of sizes <code>n</code> and <code>m</code> respectively.</p>

<p>Remove <code>list1</code>&#39;s nodes from the <code>a<sup>th</sup></code> node to the <code>b<sup>th</sup></code> node, and put <code>list2</code> in their place.</p>

<p>The blue edges and nodes in the following figure indicate the result:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/fig1.png" style="height: 130px; width: 504px;" />
<p><em>Build the result list and return its head.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/03/01/ll.png" style="width: 609px; height: 210px;" />
<pre>
<strong>Input:</strong> list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
<strong>Output:</strong> [10,1,13,1000000,1000001,1000002,5]
<strong>Explanation:</strong> We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png" style="width: 463px; height: 140px;" />
<pre>
<strong>Input:</strong> list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
<strong>Output:</strong> [0,1,1000000,1000001,1000002,1000003,1000004,6]
<strong>Explanation:</strong> The blue edges and nodes in the above figure indicate the result.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= list1.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= a &lt;= b &lt; list1.length - 1</code></li>
	<li><code>1 &lt;= list2.length &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution

[Algorithm FLOW]("blob:https://leetcode.com/8dcce3f7-f20c-4a8f-baa3-23da3d492bb4")
- The `next` of the node at index `a - 1` of `list1` points to the `head` of `list2`.
- The `next` of the `tail` of `list2` points to the node at `index b + 1` of `list1`.

##### 1. Step 1
* Find the node at index `a - 1` of list1, which we will call `start`. Set `start.next = list2`

##### 2. Step 2
* Find the node at `(original)` `index b` of list1, which we will call `end`, Set the `next` of the `tail` of `list2` to `end.next`.

```python
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1

        # Set start to node a - 1 and end to node b
        for index in range (b):
            if index == a - 1:
                start = end
            end = end.next

        # Connect the start node to list2
        start.next = list2

        # Find the tail of list2
        while (list2.next is not None):
            list2 = list2.next
        # Set the tail of list2 to end.next
        list2.next = end.next
        end.next = None
        
        return list1
```
---
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while tail.next:
            tail = tail.next
        
        cur = list1
        node = 0

        for i in range(b+1):
            next = cur.next
            if i == a-1:
                cur.next = list2
            if i == b:
                tail.next = cur.next

            cur = next
        
        return list1
```
