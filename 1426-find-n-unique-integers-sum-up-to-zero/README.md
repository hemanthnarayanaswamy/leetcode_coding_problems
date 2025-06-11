<h2><a href="https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero">1426. Find N Unique Integers Sum up to Zero</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <strong>any</strong> array containing <code>n</code> <strong>unique</strong> integers such that they add up to <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [-7,-1,1,3,4]
<strong>Explanation:</strong> These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [-1,0,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


# Solution 
* To make the sum zero every number x should have its counter part -x. 
* And to determine x if `n//2` have all the numbers from `1 - n/2` with its counter parts for n is evern. 
* When n is odd the logic is same but have a zero appended into the array 

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        for i in range(1, (n // 2)+1):
            result.append(i)
            result.append(-i)
        
        if n % 2:
            result.append(0)
        
        return result
```
