<h2><a href="https://leetcode.com/problems/merge-nodes-in-between-zeros">2299. Merge Nodes in Between Zeros</a></h2><h3>Medium</h3><hr><p>You are given the <code>head</code> of a linked list, which contains a series of integers <strong>separated</strong> by <code>0</code>&#39;s. The <strong>beginning</strong> and <strong>end</strong> of the linked list will have <code>Node.val == 0</code>.</p>

<p>For <strong>every </strong>two consecutive <code>0</code>&#39;s, <strong>merge</strong> all the nodes lying in between them into a single node whose value is the <strong>sum</strong> of all the merged nodes. The modified list should not contain any <code>0</code>&#39;s.</p>

<p>Return <em>the</em> <code>head</code> <em>of the modified linked list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/02/ex1-1.png" style="width: 600px; height: 41px;" />
<pre>
<strong>Input:</strong> head = [0,3,1,0,4,5,2,0]
<strong>Output:</strong> [4,11]
<strong>Explanation:</strong> 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/02/ex2-1.png" style="width: 600px; height: 41px;" />
<pre>
<strong>Input:</strong> head = [0,1,0,3,0,2,2,0]
<strong>Output:</strong> [1,3,4]
<strong>Explanation:</strong> 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[3, 2 * 10<sup>5</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
	<li>There are <strong>no</strong> two consecutive nodes with <code>Node.val == 0</code>.</li>
	<li>The <strong>beginning</strong> and <strong>end</strong> of the linked list have <code>Node.val == 0</code>.</li>
</ul>

# Approach
**There are no two consecutive nodes with `Node.val == 0.`**
* The `beginning` and `end` of the linked list have `Node.val == 0`.

1. We'll use 2 pointers, `zeroPointer` & `nonZeroPointer`.
2. We'll keep adding the non-zero values to the `first zeroPointer`

```python
zeroPointer = head
        nonZeroPointer = head.next

        while nonZeroPointer:
            if nonZeroPointer.val != 0:
                zeroPointer.val += nonZeroPointer.val
```
3. Now when the `nonZeroPointer` value becomes zero.
    * we skip all the nodes in-between and make `zeroPointer.next = nonZeroPointer` where zero was detected and bring the `zeroPointer` to this recent zero location. 
    * But we know at the end we also have a zero, `if nonZeroPointer.next` is valid only we follow the above steps, 
    * If `nonZeroPointer.next` becomes `NONE`, then we know we have reached the end of the Nodes, so that should be ignored, and
    * So, the recent zeroPointer's next we'll be NONE and we return `zeroPointer.next = None`

```python
else:
                if nonZeroPointer.next:
                    zeroPointer.next = nonZeroPointer
                    zeroPointer = zeroPointer.next 
                else:
                    zeroPointer.next = None
                    return head
```
---
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zeroPointer = head
        nonZeroPointer = head.next

        while nonZeroPointer:
            if nonZeroPointer.val != 0:
                zeroPointer.val += nonZeroPointer.val
            else:
                if nonZeroPointer.next:
                    zeroPointer.next = nonZeroPointer
                    zeroPointer = zeroPointer.next 
                else:
                    zeroPointer.next = None
                    return head
                
            nonZeroPointer = nonZeroPointer.next
```
---
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zeroPointer = head
        nonZeroPointer = head.next

        while nonZeroPointer and nonZeroPointer.next:
            if nonZeroPointer.val != 0:
                zeroPointer.val += nonZeroPointer.val
            else:
                zeroPointer.next = nonZeroPointer
                zeroPointer = zeroPointer.next      
            nonZeroPointer = nonZeroPointer.next
        
        zeroPointer.next = None
        return head
```
