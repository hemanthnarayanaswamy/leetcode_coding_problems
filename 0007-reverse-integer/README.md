<h2><a href="https://leetcode.com/problems/reverse-integer">7. Reverse Integer</a></h2><h3>Medium</h3><hr><p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Solution
* First need to check the number for negative if so then convert it into positive 
* covnert num into string reverse it and check for overflow and return result 

```python
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        
       
        x = int(str(x)[::-1])

        if x > 2**31:
            return 0

        return (x*-1) if negative else x
```

# Optimized Approach
```python
class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        x = abs(x)
        
        rev=0
        while(x>0):
            digit=x%10
            rev=rev*10+digit
            x=x//10

        if rev>(2**31): # need to check for only postive condition because we have converted number into positive
            return 0
        
        return rev if (temp > 0) else -rev
```
