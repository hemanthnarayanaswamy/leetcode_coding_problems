<h2><a href="https://leetcode.com/problems/power-of-three">326. Power of Three</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of three. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of three, if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 27
<strong>Output:</strong> true
<strong>Explanation:</strong> 27 = 3<sup>3</sup>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = (-1).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?

# Approach
We know that `3^19 = 1162261467` is the largest power of 3 that fits within the signed 32-bit integer range ([-2^31, 2^31 - 1] or [-2147483648, 2147483647]).

* All valid powers of 3 (like 1, 3, 9, 27, ..., 1162261467) are factors of 3^19.

* So, if n is a power of 3, it must divide 3^19 exactly — meaning 1162261467 % n == 0.

* We also check that n > 0, since powers of 3 are positive numbers only.

# Solution
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return 1162261467 % n == 0
```

---
# Using Recursion 
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False
        
        while n>1:
            if n%3==0: n=n//3
            else:
                return False
        return True
```
