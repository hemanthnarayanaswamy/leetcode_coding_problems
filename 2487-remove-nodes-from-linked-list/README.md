<h2><a href="https://leetcode.com/problems/remove-nodes-from-linked-list">2573. Remove Nodes From Linked List</a></h2><h3>Medium</h3><hr><p>You are given the <code>head</code> of a linked list.</p>

<p>Remove every node which has a node with a greater value anywhere to the right side of it.</p>

<p>Return <em>the </em><code>head</code><em> of the modified linked list.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/02/drawio.png" style="width: 631px; height: 51px;" />
<pre>
<strong>Input:</strong> head = [5,2,13,3,8]
<strong>Output:</strong> [13,8]
<strong>Explanation:</strong> The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1,1,1,1]
<strong>Output:</strong> [1,1,1,1]
<strong>Explanation:</strong> Every node has value 1, so no nodes are removed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the given list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

# Approach 
* Reverse the Linked List and then do the iteration and then before return the list reverse it again.
```
input = 5, 2, 13, 3, 8
reverse = 8, 3, 13, 2, 5

logic:
8 > 3 (remove 3) 8 13 2 5
8 !> 13 (move the pointer to 13 
13 > 2 (remove 2) 8 13 5
13 > 5 (remove 5) 8 13
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(head):
            cur = head
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        

        head = reverseLinkedList(head)
        cur = head
        nxt = cur.next
        while nxt:
            if cur.val > nxt.val:
                cur.next = nxt.next 
            else:
                cur = nxt
            nxt = nxt.next
        
        return reverseLinkedList(head)
```
* Imagine scanning the list from left to right and keeping only the values that are “safe” — meaning nothing bigger has appeared after them.
* Reversing will not be required
---
# Stack Approach 
* Maintaining the Monolithic stack.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            nxt = cur.next
            while stack and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next

        dummy = ListNode(0)
        cur = dummy 
        for i in range(len(stack)):
            cur.next = ListNode(stack[i])
            cur = cur.next
        cur.next = None

        return dummy.next
```
* You're storing the values not the **Node**
* A stack can store nodes and nodes can be reconnected

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            nxt = cur.next
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        dummy = ListNode(0)
        cur = dummy 
        for i in range(len(stack)):
            cur.next = stack[i]
            cur = cur.next
        cur.next = None

        return dummy.next
```
* Nodes that remain in the final list are in the stack, if you're popping the elements from stack, it means they will not be part of it. 
* You push the nodes, as the pushed nodes will be part of the final node
* The top of the stack is always the previous node in the final list
* If you maintain `next` pointer correctly, the stack's bottom is the final `head`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
            
            if stack:
                stack[-1].next = cur
                
            stack.append(cur)
            cur = cur.next
        
        return stack[0]
```
---
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head

        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()

            if stack:
                stack[-1].next = cur
            stack.append(cur)

            cur = cur.next
            stack[-1].next = None

        return stack[0]
```
