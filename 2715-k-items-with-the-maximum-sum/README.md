<h2><a href="https://leetcode.com/problems/k-items-with-the-maximum-sum">2715. K Items With the Maximum Sum</a></h2><h3>Easy</h3><hr><p>There is a bag that consists of items, each item&nbsp;has a number <code>1</code>, <code>0</code>, or <code>-1</code> written on it.</p>

<p>You are given four <strong>non-negative </strong>integers <code>numOnes</code>, <code>numZeros</code>, <code>numNegOnes</code>, and <code>k</code>.</p>

<p>The bag initially contains:</p>

<ul>
	<li><code>numOnes</code> items with <code>1</code>s written on them.</li>
	<li><code>numZeroes</code> items with <code>0</code>s written on them.</li>
	<li><code>numNegOnes</code> items with <code>-1</code>s written on them.</li>
</ul>

<p>We want to pick exactly <code>k</code> items among the available items. Return <em>the <strong>maximum</strong> possible sum of numbers written on the items</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
It can be proven that 2 is the maximum possible sum.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
It can be proven that 3 is the maximum possible sum.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

# Solution 
* Simple Problem, Don't complicate it, You can build the array and when take the sum  of thatt array of `k` elements. 

```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        items = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes

        return sum(items[:k])
```
---
```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0

        while k:
            if numOnes:
                res += 1
                numOnes -= 1
            elif numZeros:
                numZeros -= 1
            else:
                res -= 1
                numNegOnes -= 1
            
            k -= 1
        
        return res
```
---
```python
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        maxi = 0
        for i in range(k):
            if numOnes > 0:
                maxi += 1
                numOnes -=1
            else:
                if numZeros > 0:
                    numZeros -= 1
                else:
                    maxi -= 1
        return maxi
```

<ul>
	<li><code>0 &lt;= numOnes, numZeros, numNegOnes &lt;= 50</code></li>
	<li><code>0 &lt;= k &lt;= numOnes + numZeros + numNegOnes</code></li>
</ul>
