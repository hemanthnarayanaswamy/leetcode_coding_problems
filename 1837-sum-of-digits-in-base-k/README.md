<h2><a href="https://leetcode.com/problems/sum-of-digits-in-base-k">1965. Sum of Digits in Base K</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code> (in base <code>10</code>) and a base <code>k</code>, return <em>the <strong>sum</strong> of the digits of </em><code>n</code><em> <strong>after</strong> converting </em><code>n</code><em> from base </em><code>10</code><em> to base </em><code>k</code>.</p>

<p>After converting, each digit should be interpreted as a base <code>10</code> number, and the sum should be returned in base <code>10</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 34, k = 6
<strong>Output:</strong> 9
<strong>Explanation: </strong>34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10, k = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>n is already in base 10. 1 + 0 = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 10</code></li>
</ul>

# Approach
1. Conversion from `base 10 to base 6` can be done by **dividing the number by 6 until the quotient is 0.**
```ini
34 divides 6, Quotient = 5, remaining = 4
5 divides 6, Quotient = 0, remaining =5
```
* until `quotient` keep dividing it by `k` and keep adding the `r` remainder to the result and return the result after the iteration.

```python
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        q, r = divmod(n, k)
        res = r

        while q:
            q, r = divmod(q,k)
            res += r
            
        return res
```
---
```python
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0

        while n:
            res += n % k
            n //= k
        
        return res
```
