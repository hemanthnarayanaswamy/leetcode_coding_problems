<h2><a href="https://leetcode.com/problems/maximum-difference-by-remapping-a-digit">2704. Maximum Difference by Remapping a Digit</a></h2><h3>Easy</h3><hr><p>You are given an integer <code>num</code>. You know that Bob will sneakily <strong>remap</strong> one of the <code>10</code> possible digits (<code>0</code> to <code>9</code>) to another digit.</p>

<p>Return <em>the difference between the maximum and minimum&nbsp;values Bob can make by remapping&nbsp;<strong>exactly</strong> <strong>one</strong> digit in </em><code>num</code>.</p>

<p><strong>Notes:</strong></p>

<ul>
	<li>When Bob remaps a digit <font face="monospace">d1</font>&nbsp;to another digit <font face="monospace">d2</font>, Bob replaces all occurrences of <code>d1</code>&nbsp;in <code>num</code>&nbsp;with <code>d2</code>.</li>
	<li>Bob can remap a digit to itself, in which case <code>num</code>&nbsp;does not change.</li>
	<li>Bob can remap different digits for obtaining minimum and maximum values respectively.</li>
	<li>The resulting number after remapping can contain leading zeroes.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 11891
<strong>Output:</strong> 99009
<strong>Explanation:</strong> 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 90
<strong>Output:</strong> 99
<strong>Explanation:</strong>
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>

# Solution 

#### Key Insights:
1. Maximum Number: Replace first non-'9' digit with '9'
2. Minimum Number: Replace first non-'0' digit with '0' (avoid leading zeros)
3. Single Pass: Find both replacement digits in one loop

```ini
Algorithm Steps

1. Convert to String: Easy digit manipulation
2. Single Pass Search: Find both replacement candidates
3. Early Termination: Break when both digits found
4. Handle Edge Cases: All 9s or all 0s
```
```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        numStr = str(num)
        replace_digit1 = None
        replace_digit2 = None

        for d in numStr:
            if replace_digit1 is None and d != '9':
                replace_digit1 = d
            
            
            if replace_digit2 is None and d != '0':
                replace_digit2 = d
            
            
            if replace_digit1 is not None and replace_digit2 is not None:
                break

        if replace_digit2:
            min_num = int(numStr.replace(replace_digit2, '0'))
        else:
            min_num = num
        
        if replace_digit1:
            max_num = int(numStr.replace(replace_digit1, '9'))
        else:
            max_num = num

        return max_num - min_num
```
# Improved Solution 
```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        numStr = str(num)
        replace_digit1 = replace_digit2 = None
        
        for d in numStr:
            if replace_digit1 is None and d != '9':
                replace_digit1 = d
            if replace_digit2 is None and d != '0':
                replace_digit2 = d
            if replace_digit1 and replace_digit2:  
                break
        
        max_num = int(numStr.replace(replace_digit1, '9')) if replace_digit1 else num
        min_num = int(numStr.replace(replace_digit2, '0')) if replace_digit2 else num
        
        return max_num - min_num
```

# Optimal Solution 
```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        minimal = int(s.replace(s[0], '0'))

        x = '9'
        for c in s:
            if c != '9':
                x = c
                break
        
        maximal = int(s.replace(x, '9'))

        return maximal - minimal
```
