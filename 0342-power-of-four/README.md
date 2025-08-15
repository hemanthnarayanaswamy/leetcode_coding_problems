<h2><a href="https://leetcode.com/problems/power-of-four">342. Power of Four</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of four. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of four, if there exists an integer <code>x</code> such that <code>n == 4<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?

# Solution 
* Remove all negative numbers. 
* Apply the loop for only numbers greater then 1.

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n > 1:
            while n > 1:
                if n % 4 != 0:
                    return False
                n //= 4
        else:
            return False
        
        return True
```

# Optimal Solution 
```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        i=0
        while True:
            temp = 4**i
            if temp==n:
                return True
            elif temp>n:
                return False
            i+=1
```

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n==1 or n!=0==n%4 and self.isPowerOfFour(n//4)
```
