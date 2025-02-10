<h2><a href="https://leetcode.com/problems/plus-one">66. Plus One</a></h2><h3>Easy</h3><hr><p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>&#39;s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>&#39;s.</li>
</ul>


### My approach 

1. I try to use the if statement to work on all the different conditions that can occuer and retured digits 
2. But that logic covered mejority of the test but it failed few edge cases where they are multiple `9` in the digits 

```python 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lenght_digits = len(digits)
    
        if lenght_digits:
            last_digit = digits[-1]
            first_digit = digits[0]
        else:
            return [1]


        if lenght_digits > 1 and last_digit == 9:
            digits[-1] = 0
            digits[0] += 1
        elif lenght_digits > 1 and last_digit != 9:
            digits[-1] += 1
            
        elif lenght_digits == 1 and first_digit == 9:
            return [1, 0]
        else:
            digits[0] += 1

        return digits
```
* Useless Efforts seriously on a simple problem, need to learn addition first and how carry works to solve it. 

```python 
def plusOne(digits):
    n = len(digits)

    # Traverse from the last digit
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1  # Increment the current digit
            return digits  # Return early (no need to modify other digits)
        digits[i] = 0  # Set current digit to 0 (carry to next)

    # If all digits were 9 (e.g., [9,9,9] → [1,0,0,0])
    return [1] + digits
```

* Improve the solution

```python 
result = ''.join(map(str,digits)) ## my approach that didn't work
        new = int(result) 
        new = new + 1

        array = [int(digit) for digit in str(new)] 
        return array
```
