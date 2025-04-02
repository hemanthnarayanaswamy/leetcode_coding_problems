<h2><a href="https://leetcode.com/problems/add-digits">258. Add Digits</a></h2><h3>Easy</h3><hr><p>Given an integer <code>num</code>, repeatedly add all its digits until the result has only one digit, and return it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 38
<strong>Output:</strong> 2
<strong>Explanation:</strong> The process is
38 --&gt; 3 + 8 --&gt; 11
11 --&gt; 1 + 1 --&gt; 2 
Since 2 has only one digit, return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without any loop/recursion in <code>O(1)</code> runtime?</p>


# Solution Approach 
* When faced with the problem of repeatedly summing the digits of a number until a single digit is obtained, it may initially seem that we need to iteratively sum the digits. However, there is a mathematical shortcut related to digital roots that can be leveraged to solve this problem more efficiently.

1. If the input number num is 0, the result is 0 because the digital root of 0 is 0.
2. If num is divisible by 9, return 9. This is because any number that is a multiple of 9 has a digital root of 9 (except for 0).
3. For all other numbers, return num % 9. This remainder gives the digital root directly. This is based on the properties of numbers and modulo arithmetic, which simplifies the process to a constant-time solution.

```python 
class Solution(object):
    def addDigits(self, num):
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)       
```

## Loop Approach 
```python
class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        
        while len(num_str) > 1:
            temp_sum = 0
            print(temp_sum, num_str)
            for digits in num_str:
                temp_sum += int(digits)   
            num_str = str(temp_sum)
        
        return int(num_str)
```
