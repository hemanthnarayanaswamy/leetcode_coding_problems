<h2><a href="https://leetcode.com/problems/count-operations-to-obtain-zero">2288. Count Operations to Obtain Zero</a></h2><h3>Easy</h3><hr><p>You are given two <strong>non-negative</strong> integers <code>num1</code> and <code>num2</code>.</p>

<p>In one <strong>operation</strong>, if <code>num1 &gt;= num2</code>, you must subtract <code>num2</code> from <code>num1</code>, otherwise subtract <code>num1</code> from <code>num2</code>.</p>

<ul>
	<li>For example, if <code>num1 = 5</code> and <code>num2 = 4</code>, subtract <code>num2</code> from <code>num1</code>, thus obtaining <code>num1 = 1</code> and <code>num2 = 4</code>. However, if <code>num1 = 4</code> and <code>num2 = 5</code>, after one operation, <code>num1 = 4</code> and <code>num2 = 1</code>.</li>
</ul>

<p>Return <em>the <strong>number of operations</strong> required to make either</em> <code>num1 = 0</code> <em>or</em> <code>num2 = 0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 2, num2 = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
- Operation 1: num1 = 2, num2 = 3. Since num1 &lt; num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 &gt; num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 10, num2 = 10
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num1, num2 &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
* Before going into the loop make sure both the numbers are non-zero with `and` condition 

```python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0

        while num1 and num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            
            result += 1
        
        return result 
```

# Optimal Solution 
* You can avoid the potentially O(max(num1, num2)) “subtract one at a time” loop by batching subtractions using integer division and modulus. This brings you down to roughly O(log min(num1, num2)) time—essentially the same complexity as the classic Euclidean GCD algorithm.
* Each loop now reduces one operand by at least a factor of two (on average), giving you a logarithmic number of steps—much smaller than subtracting 1 repeatedly.

```python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations =0
        while(num1 != 0 and num2!=0 ):
            if(num1 >= num2):
                operations += num1 // num2
                num1 %= num2
            else:
                operations += num2 // num1 
                num2 %= num1 
        return operations
```

```python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        # keep subtracting the smaller from the larger in bulk
        while num1 and num2:
            if num1 >= num2:
                # subtract num2 as many times as possible in one go
                q, num1 = divmod(num1, num2)  # does the same in one C-level operation (q = num1 // num2 and num1 %= num2).
                count += q
            else:
                q, num2 = divmod(num2, num1)
                count += q
        return count
```
