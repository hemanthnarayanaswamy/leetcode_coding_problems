<h2><a href="https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i">3543. Count Substrings That Satisfy K-Constraint I</a></h2><h3>Easy</h3><hr><p>You are given a <strong>binary</strong> string <code>s</code> and an integer <code>k</code>.</p>

<p>A <strong>binary string</strong> satisfies the <strong>k-constraint</strong> if <strong>either</strong> of the following conditions holds:</p>

<ul>
	<li>The number of <code>0</code>&#39;s in the string is at most <code>k</code>.</li>
	<li>The number of <code>1</code>&#39;s in the string is at most <code>k</code>.</li>
</ul>

<p>Return an integer denoting the number of <span data-keyword="substring-nonempty">substrings</span> of <code>s</code> that satisfy the <strong>k-constraint</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;10101&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>Every substring of <code>s</code> except the substrings <code>&quot;1010&quot;</code>, <code>&quot;10101&quot;</code>, and <code>&quot;0101&quot;</code> satisfies the k-constraint.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1010101&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">25</span></p>

<p><strong>Explanation:</strong></p>

<p>Every substring of <code>s</code> except the substrings with a length greater than 5 satisfies the k-constraint.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;11111&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>All substrings of <code>s</code> satisfy the k-constraint.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50 </code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

# Solution
* We need to count the number of substrings in s such that the number of `0's & 1's` in each substring does not exceed `k`.
*  we can use a sliding window approach to count the number of substrings, going from an exponential complexity to linear `(O(n))`. 
*  We use `l & r` to represent the boundaries for each window. Also, we use `ones` and `zeros` to represent the counts for the number of ones and zeros and each substring/window.

**We expand the window in each iteration and increment ones and zeros accordingly. If at any point both ones and zeros becomes greater than k, we shrink the window from the left side while also decrementing ones and zeros accordingly.**

- Then at the end of each iteration, we add the number of subarrays that we can create out of the current window (represented by `r - l + 1`) to res

```ini
* When your window is valid, it covers the substring: s[start: i]
The window has length is i - start + 1

Every substring that ends at index i and starts anywhere between  start and i is valid

If the window is start ... i

Then the valid substrings ending at i are:
s[i:i+1]
s[i-1:i+1]
s[i-2:i+1]
...
s[start:i+1] # How many substring is that

Count the starting Positions:         start, start+1, ..., i
That’s exactly:                                i - start + 1
```
---
```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zeroCount = oneCount = 0
        res = 0
        start = 0

        for i in range(len(s)):
            if s[i] == '1':
                oneCount += 1
            else:
                zeroCount += 1
            
            while zeroCount > k and oneCount > k:
                if s[start] == '1':
                    oneCount -= 1
                else:
                    zeroCount -= 1
                start += 1
            res += i - start + 1
        
        return res
```
