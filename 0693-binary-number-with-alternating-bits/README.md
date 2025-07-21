<h2><a href="https://leetcode.com/problems/binary-number-with-alternating-bits">693. Binary Number with Alternating Bits</a></h2><h3>Easy</h3><hr><p>Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary representation of 5 is: 101
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary representation of 7 is: 111.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary representation of 11 is: 1011.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Solution 
* First convert the number into binary and check if `11 or 00` exists in that converted string. 

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binaryVal = bin(n)

        return False if '00' in binaryVal or '11' in binaryVal else True
```
# Optimal Solution 
* Use bit manipulation 

```ini
If the bits alternate, then

n    = b_k b_{k-1} … b_1 b_0
n>>1 = 0  b_k   b_{k-1} … b_1

XOR’ing those gives all 1’s:
x = n ^ (n >> 1) = 111…111₂
And any number of the form 111…111₂ satisfies x & (x+1) == 0.
```


