<h2><a href="https://leetcode.com/problems/number-of-even-and-odd-bits">2659. Number of Even and Odd Bits</a></h2><h3>Easy</h3><hr><p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>Let <code>even</code> denote the number of even indices in the binary representation of <code>n</code> with value 1.</p>

<p>Let <code>odd</code> denote the number of odd indices in the binary representation of <code>n</code> with value 1.</p>

<p>Note that bits are indexed from <strong>right to left</strong> in the binary representation of a number.</p>

<p>Return the array <code>[even, odd]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 50</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 50 is <code>110010</code>.</p>

<p>It contains 1 on indices 1, 4, and 5.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 2 is <code>10</code>.</p>

<p>It contains 1 only on index 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

**Note: Indices of binary representations start from the right. 
* So to make the binary representation meet the index of the programming language reverse the string. 

```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binN = bin(n)[2::][::-1]
        res = [0, 0]

        for i in range(len(binN)):
            if binN[i] == '1':
                if i % 2:
                   res[1] += 1
                else:
                    res[0] += 1
        
        return res
```

# Optimal Bit Manipulation Solution 
```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        index = 0
        
        while n > 0:
            if n & 1:  # check if the current rightmost bit is 1
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1  # right shift to move to the next bit
            index += 1
        
        return [even, odd]
```
