<h2><a href="https://leetcode.com/problems/sqrtx">69. Sqrt(x)</a></h2><h3>Easy</h3><hr><p>Given a non-negative integer <code>x</code>, return <em>the square root of </em><code>x</code><em> rounded down to the nearest integer</em>. The returned integer should be <strong>non-negative</strong> as well.</p>

<p>You <strong>must not use</strong> any built-in exponent function or operator.</p>

<ul>
	<li>For example, do not use <code>pow(x, 0.5)</code> in c++ or <code>x ** 0.5</code> in python.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 4 is 2, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Solution 
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0

        if x <= 3:
            return 1

        l, r = 2, x//2

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1

        return r
```
After this loop style `(while l <= r, with l = mid + 1 / r = mid - 1)`, the clean invariant is:
* `r` ends as the largest value whose square is `<= x`.

---
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            midsq = mid * mid

            if midsq == x:
                return mid
            elif midsq > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans
```

## Approach: Binary Search

1. `Search space:` Consider all integers from 0 to x as potential square roots
2. `Middle calculation:` Compute mid and check if mid² equals, exceeds, or is less than x
3. `Exact match:` If `mid² == x`, we found the exact square root
4. Too large: If `mid² > x`, search smaller values `(right = mid - 1)`
5. Candidate found: If `mid² < x`, save mid as potential answer and search larger values
