<h2><a href="https://leetcode.com/problems/sequential-digits">1212. Sequential Digits</a></h2><h3>Medium</h3><hr><p>An&nbsp;integer has <em>sequential digits</em> if and only if each digit in the number is one more than the previous digit.</p>

<p>Return a <strong>sorted</strong> list of all the integers&nbsp;in the range <code>[low, high]</code>&nbsp;inclusive that have sequential digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> low = 100, high = 300
<strong>Output:</strong> [123,234]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> low = 1000, high = 13000
<strong>Output:</strong> [1234,2345,3456,4567,5678,6789,12345]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= low &lt;= high &lt;= 10^9</code></li>
</ul>

## Solution Approach 

* I complicated the problem a bit but the approach is simple math logic 
* We construct numbers dynamically by multiplying by 10 and adding the next digits.
```
	1*10 + 2 = 12
	12*10 + 3 = 123
	123 * 10 + 4 = 1234
```
* Than we check if the generated number is within the high and low range. 

```python 
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = [] # store results 

        for i in range(1, 10): # To generate all possible numbers
            num = i
            
            for j in range(i+1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    result.append(num)

        return sorted(result) 
```
