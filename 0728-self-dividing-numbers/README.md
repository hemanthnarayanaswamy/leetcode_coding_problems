<h2><a href="https://leetcode.com/problems/self-dividing-numbers">728. Self Dividing Numbers</a></h2><h3>Easy</h3><hr><p>A <strong>self-dividing number</strong> is a number that is divisible by every digit it contains.</p>

<ul>
	<li>For example, <code>128</code> is <strong>a self-dividing number</strong> because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.</li>
</ul>

<p>A <strong>self-dividing number</strong> is not allowed to contain the digit zero.</p>

<p>Given two integers <code>left</code> and <code>right</code>, return <em>a list of all the <strong>self-dividing numbers</strong> in the range</em> <code>[left, right]</code> (both <strong>inclusive</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> left = 1, right = 22
<strong>Output:</strong> [1,2,3,4,5,6,7,8,9,11,12,15,22]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> left = 47, right = 85
<strong>Output:</strong> [48,55,66,77]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>4</sup></code></li>
</ul>

# Solution 
* Use a helper function to get the division results 

```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        def helperDividing(num):
            temp = str(num)

            if '0' in temp: # avoid numbers with 0 in it avoid modulo by zero error
                return 

            for n in temp:
                if num % int(n) != 0:
                    return 
            return num

        for num in range(left, right+1):
            res = helperDividing(num)
            if res:
                result.append(res)
        
        return result
```

* Always and final note avoid converting the numbers into string for digit division use the modulo 10 formula to get each digits.

# Improved Solution
```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        def helperDividing(num):
            temp = num

            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return
                temp //= 10
            
            return num

        for num in range(left, right+1):
            res = helperDividing(num)
            if res:
                result.append(res)
        
        return result
```

# OPTIMAL SOLUTION
```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for num in range(left, right + 1):
            tmp = num
            while tmp:
                d = tmp % 10
                # if digit is 0 or doesn't divide num, bail out
                if d == 0 or num % d:
                    break
                tmp //= 10
            else:
                # only executed if while loop didn't break
                res.append(num)

        return res
```
