<h2><a href="https://leetcode.com/problems/intersection-of-two-linked-lists">160. Intersection of Two Linked Lists</a></h2><h3>Easy</h3><hr><p>Given the heads of two singly linked-lists <code>headA</code> and <code>headB</code>, return <em>the node at which the two lists intersect</em>. If the two linked lists have no intersection at all, return <code>null</code>.</p>

<p>For example, the following two linked lists begin to intersect at node <code>c1</code>:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png" style="width: 500px; height: 162px;" />
<p>The test cases are generated such that there are no cycles anywhere in the entire linked structure.</p>

<p><strong>Note</strong> that the linked lists must <strong>retain their original structure</strong> after the function returns.</p>

<p><strong>Custom Judge:</strong></p>

<p>The inputs to the <strong>judge</strong> are given as follows (your program is <strong>not</strong> given these inputs):</p>

<ul>
	<li><code>intersectVal</code> - The value of the node where the intersection occurs. This is <code>0</code> if there is no intersected node.</li>
	<li><code>listA</code> - The first linked list.</li>
	<li><code>listB</code> - The second linked list.</li>
	<li><code>skipA</code> - The number of nodes to skip ahead in <code>listA</code> (starting from the head) to get to the intersected node.</li>
	<li><code>skipB</code> - The number of nodes to skip ahead in <code>listB</code> (starting from the head) to get to the intersected node.</li>
</ul>

<p>The judge will then create the linked structure based on these inputs and pass the two heads, <code>headA</code> and <code>headB</code> to your program. If you correctly return the intersected node, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="width: 500px; height: 162px;" />
<pre>
<strong>Input:</strong> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
<strong>Output:</strong> Intersected at &#39;8&#39;
<strong>Explanation:</strong> The intersected node&#39;s value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node&#39;s value is not 1 because the nodes with value 1 in A and B (2<sup>nd</sup> node in A and 3<sup>rd</sup> node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3<sup>rd</sup> node in A and 4<sup>th</sup> node in B) point to the same location in memory.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="width: 500px; height: 194px;" />
<pre>
<strong>Input:</strong> intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong>Output:</strong> Intersected at &#39;2&#39;
<strong>Explanation:</strong> The intersected node&#39;s value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png" style="width: 300px; height: 189px;" />
<pre>
<strong>Input:</strong> intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
<strong>Output:</strong> No intersection
<strong>Explanation:</strong> From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes of <code>listA</code> is in the <code>m</code>.</li>
	<li>The number of nodes of <code>listB</code> is in the <code>n</code>.</li>
	<li><code>1 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= skipA &lt;= m</code></li>
	<li><code>0 &lt;= skipB &lt;= n</code></li>
	<li><code>intersectVal</code> is <code>0</code> if <code>listA</code> and <code>listB</code> do not intersect.</li>
	<li><code>intersectVal == listA[skipA] == listB[skipB]</code> if <code>listA</code> and <code>listB</code> intersect.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you write a solution that runs in <code>O(m + n)</code> time and use only <code>O(1)</code> memory?

# Solution 

1. If the lenght of the two linked list is the same, then we can check each node and keep moving forward until we get the intersection point, If there is no intersection point then it returns `NONE`

**How can we make the two lists the same lenght ?**

```ini
A: 4 → 1 → 8
B: 5 → 6 → 1 → 8

- The Strategy is to connect both lists with each other.
A: 4 → 1 → 8 → 5 → 6 → 1 → 8
B: 5 → 6 → 1 → 8 → 4 → 1 → 8

- When we reach end of lists, go back to head of other list, so that we can find intersection at some point.
```
---
```ini
                           B→→→→→→→→→→→→
A: 4 → 1 → 8 → 4 → 5 → n → 5 → 6 → 1 → 8
B: 5 → 6 → 1 → 8 → 4 → 5 → n → 4 → 1 → 8
                               A→→→→→→→→
n is null

                   B→→→→→→→→
A: 2 → 6 → 4 → n → 1 → 5 → n
B: 1 → 5 → n → 2 → 6 → 4 → n
               A→→→→→→→→→→→→
n is null
```
---
```python
# Definition for singly-linked list.
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = headA
        listB = headB

        while listA != listB:
            listA = listA.next if listA else headB
            listB = listB.next if listB else headA
        
        return listA
```
---
1. Two pointers, `lista` and `listb`, are initialized to the heads of the two input linked lists `(headA and headB)`. These pointers will traverse the lists to find the intersection point.
2. `while lista != listb:`, The loop continues as long as `lista` and `listb` do not point to the same node. 
    - If there is an intersection, they will eventually meet at the intersecting node. 
    - If not, both pointers will reach None at the same time, breaking the loop.
3. If `lista` is not `None`, it moves to the `next node` `(lista.next)`. Otherwise, it switches to the head of the other list `(headB)`.
   - Similarly, if `listb` is not `None`, it moves to the `next node` (listb.next). Otherwise, it switches to the head of the other list `(headA)`.

**When a pointer reaches the end of one list and switches to the other, the difference in lengths between the two lists is neutralized. This ensures that both pointers traverse the same total distance before meeting.**

4. At this point, the loop has exited, `meaning lista and listb are pointing to the same node`.
   - If there is an intersection, this node is the intersecting node. If there is no intersection, `both pointers are None`, and the function returns `None`.

