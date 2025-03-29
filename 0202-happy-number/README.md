<h2><a href="https://leetcode.com/problems/happy-number">202. Happy Number</a></h2><h3>Easy</h3><hr><p>Write an algorithm to determine if a number <code>n</code> is happy.</p>

<p>A <strong>happy number</strong> is a number defined by the following process:</p>

<ul>
	<li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
	<li>Repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1.</li>
	<li>Those numbers for which this process <strong>ends in 1</strong> are happy.</li>
</ul>

<p>Return <code>true</code> <em>if</em> <code>n</code> <em>is a happy number, and</em> <code>false</code> <em>if not</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## Solution Approach 
* If the number repeats itself in the process then its not a happy number, we define a set to keep track of all the number we encounter then return False if a number in that set is detected again. 
* WE do the algorithm and if the result is `1` we return True 

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        unique_result = set()
        while n not in unique_result:
            unique_result.add(n)
            temp_sum = 0
            for num in str(n):
                temp_sum += int(num)**2
            
            if temp_sum == 1:
                return True
            else:
                n = temp_sum
    
        return False
```
