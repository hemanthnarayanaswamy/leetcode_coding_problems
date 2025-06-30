<h2><a href="https://leetcode.com/problems/find-the-pivot-integer">2571. Find the Pivot Integer</a></h2><h3>Easy</h3><hr><p>Given a positive integer <code>n</code>, find the <strong>pivot integer</strong> <code>x</code> such that:</p>

<ul>
	<li>The sum of all elements between <code>1</code> and <code>x</code> inclusively equals the sum of all elements between <code>x</code> and <code>n</code> inclusively.</li>
</ul>

<p>Return <em>the pivot integer </em><code>x</code>. If no such integer exists, return <code>-1</code>. It is guaranteed that there will be at most one pivot index for the given input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 is the pivot integer since: 1 = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proved that no such integer exist.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

# Solution 
* We need to use the Prefix Sum technique to find the left and right sum at every interger in the `range(1, n)`
* Right Sum will be `totalSum - leftSum` and left sum will be `Previous left sum + current Interger`
* Check if both sum are equal then return the interger 

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        leftSum = 0
        rightSum = 0

        totalSum = sum(range(1, n+1))

        for i in range(1, n+1):
            rightSum = totalSum - leftSum 
            leftSum += i

            if rightSum == leftSum:
                return i 
        
        return -1
```

## Improved Solution 
```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        leftSum = 0
        rightSum = 0

        totalSum = n * (n+1)//2

        for i in range(1, n+1):
            rightSum = totalSum - leftSum 
            leftSum += i

            if rightSum == leftSum:
                return i 
        
        return -1
```

# Optimal Solution
```python
import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        S = n * (n + 1) // 2
        i = math.isqrt(S)           # integer square root of S
        return i if i * i == S else -1
```
![image](https://github.com/user-attachments/assets/c8206b20-cf81-41c1-8394-b5c5d665c68b)


