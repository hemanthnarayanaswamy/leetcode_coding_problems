<h2><a href="https://leetcode.com/problems/add-two-numbers">2. Add Two Numbers</a></h2><h3>Medium</h3><hr><p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

# Solution 
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(a, b, c):
            res = a+b+c
            if res >= 10:
                n = res % 10
                c = res // 10
            else:
                n = res
                c = 0
            return n, c
        
        dummy = ListNode(0)
        cur = dummy
        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2:
            if p1 and p2:
                n, c = add(p1.val, p2.val, carry)
                p1 = p1.next
                p2 = p2.next
            elif p1 and not p2:
                n, c = add(p1.val, 0, carry)
                p1 = p1.next
            else:
                n, c = add(0, p2.val, carry)
                p2 = p2.next
            
            cur.next = ListNode(n)
            carry = c
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)
            cur = cur.next
        cur.next = None

        return dummy.next
```
* At the end is the `carry` remains make sure to add it as a tail before Ending the linked list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            res = a + b + carry
            carry, num = divmod(res, 10)
                
            cur.next = ListNode(num)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        cur.next = None

        return dummy.next
```            
