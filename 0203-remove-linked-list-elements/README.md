<h2><a href="https://leetcode.com/problems/remove-linked-list-elements">203. Remove Linked List Elements</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a linked list and an integer <code>val</code>, remove all the nodes of the linked list that has <code>Node.val == val</code>, and return <em>the new head</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong>Output:</strong> [1,2,3,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [], val = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [7,7,7,7], val = 7
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 50</code></li>
</ul>

# Solution 
1. We'll make sure to land on a node on which `head` is not the `val`. 
```python
while head and head.val == val:
            head = head.next
```
2. Next as usual we define `curr, prev` and start the iteration and when `cur.val == val`, and try to remove the node by assinging `pre.next = cur.next` skip current node 

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head and head.val == val:
            head = head.next
    
        if head and head.next:
            prev = head
            curr = head.next

            while curr:
                if curr.val == val:
                    prev.next = curr.next
                else:
                    prev = curr
                curr = curr.next
                
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
    def removeElements(self, head, val):
        dummy = ListNode(0, head)   # Dummy node pointing to head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next   # Remove node
            else:
                current = current.next

        return dummy.next
```

1. Step 1 - Creating a Dummy Node:👈
		  * A new ListNode named 'temp' is created with a value of 0. This node serves as a dummy head node to simplify edge cases, especially when the head node itself needs to be removed.
		  * 'curr' is a reference that initially points to the same dummy node.
			* The next of 'temp' is set to head, effectively inserting the dummy node before the actual head of the list.
			`ListNode temp = new ListNode(0) , curr = temp; temp.next = head; 

2. Step 2 - Iterating through the List: 👈
* The loop continues as long as the next node after 'curr' is not null.
* Inside the loop, it checks if the val of the next node (curr.next.val) is equal to the target value val.
* If it is, 'curr.next' is updated to 'curr.next.next', effectively removing the current next node from the list.
* If it is not, curr is moved to the next node in the list.
