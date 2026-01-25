<h2><a href="https://leetcode.com/problems/remove-zeros-in-decimal-representation">4051. Remove Zeros in Decimal Representation</a></h2><h3>Easy</h3><hr><p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>Return the integer obtained by removing all zeros from the decimal representation of <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1020030</span></p>

<p><strong>Output:</strong> <span class="example-io">123</span></p>

<p><strong>Explanation:</strong></p>

<p>After removing all zeros from 1<strong><u>0</u></strong>2<strong><u>00</u></strong>3<strong><u>0</u></strong>, we get 123.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>1 has no zero in its decimal representation. Therefore, the answer is 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>15</sup></code></li>
</ul>

# Solution 
```python
class Solution:
    def removeZeros(self, n: int) -> int:
        res = []

        while n:
            quotient, remainder = divmod(n, 10)
            if remainder:
                res.append(str(remainder))
            n = quotient
        
        return int(''.join(res[::-1]))
```
---
```python
class Solution:
    def removeZeros(self, n: int) -> int:
        res = []

        for i in str(n):
            if i != '0':
                res.append(i)
        
        return int(''.join(res))
```
---
```python
class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0

        for i in str(n):
            if i != '0':
                res = res * 10 + int(i)
        
        return res
```
---
```python
class Solution(object):
    def removeZeros(self, n: int) -> int:
        s = ""
        while n:
            rem = n % 10
            if rem != 0:
                s = s + str(rem)
            n //= 10
        s = s[::-1]
        return int(s)
```
