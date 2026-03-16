<h2><a href="https://leetcode.com/problems/reorder-list">143. Reorder List</a></h2><h3>Medium</h3><hr><p>You are given the head of a singly linked-list. The list can be represented as:</p>

<pre>
L<sub>0</sub> &rarr; L<sub>1</sub> &rarr; &hellip; &rarr; L<sub>n - 1</sub> &rarr; L<sub>n</sub>
</pre>

<p><em>Reorder the list to be on the following form:</em></p>

<pre>
L<sub>0</sub> &rarr; L<sub>n</sub> &rarr; L<sub>1</sub> &rarr; L<sub>n - 1</sub> &rarr; L<sub>2</sub> &rarr; L<sub>n - 2</sub> &rarr; &hellip;
</pre>

<p>You may not modify the values in the list&#39;s nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>

# Solution

```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Use Floyd's Slow and Fast pointers approach
        # use slow and fast pointers to split the given list into two (slow = 0, fast = 1)
        # reverse the directions in second part of the list 
        # then, use two pointers to merge two lists: one from beginning of first list (left to right) and 
        # another one from end of second list (but traverse from right to left since directions are flipped)
        
        slow, fast = head, head.next
        
        # use slow and fast to split the given list into two lists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # beginning of second half is after slow (when fast is at null or reached to the last element in the list)
        second = slow.next
        slow.next = None # this is assigning the last node.next to null from the first part of the list (if not, there will be a cycle)
        prev = None
        # reverse the second part of the list (directions)
        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp
            
        # merge two halfs of the list
        # after prev while loop, prev will be at the last node of second list
        first, second = head, prev
        # second half of the list can be shorter if the given list is odd so it can reach to null before first
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

```
