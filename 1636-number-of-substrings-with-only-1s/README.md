<h2><a href="https://leetcode.com/problems/number-of-substrings-with-only-1s">1636. Number of Substrings With Only 1s</a></h2><h3>Medium</h3><hr><p>Given a binary string <code>s</code>, return <em>the number of substrings with all characters</em> <code>1</code><em>&#39;s</em>. Since the answer may be too large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110111&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are 9 substring in total with only 1&#39;s characters.
&quot;1&quot; -&gt; 5 times.
&quot;11&quot; -&gt; 3 times.
&quot;111&quot; -&gt; 1 time.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;101&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring &quot;1&quot; is shown 2 times in s.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;111111&quot;
<strong>Output:</strong> 21
<strong>Explanation:</strong> Each substring contains only 1&#39;s characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

# Solution 
**Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is 
`(n + 1) * n // 2`.**
**The number of substrings in `11111` is `n * (n+1) // 2`
* First, start the continous count of ones, when the ones streak break at that point calculate the number of substrings using the above formula
```
Example 1: "0110111"
* First we start to iterate, we find `11` initially then the streak breaks, so we calculate the substrings as `2 * 3 // 2 = 3`
* Next we continue and at the end we find the `111` substring, `3 * 4 // 2 = 6`
* Total substring with only 1's is `3 + 6 = 9`

Example 2: "111111"
* Total one's count is 6 --> `6 * 7 // 2 = 21`
* Total substring with only 1's is `21`
```
---
```python
class Solution:
    def numSub(self, s: str) -> int:
        totalSubstrings = 0
        onesCount = 0
        MOD = 10**9 + 7

        for c in s:
            if c == '1':
                onesCount += 1
            else:
                totalSubstrings += (onesCount * (onesCount + 1))// 2
                onesCount = 0
        
        totalSubstrings += (onesCount * (onesCount + 1))// 2

        return totalSubstrings % MOD
```
---
```python
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        run = 0
        
        for ch in s:
            if ch == '1':
                run += 1
            else:
                total += (run * (run+1)) // 2
                run = 0
                if total > MOD: 
                    total %= MOD
        
        total += (run * (run+1)) // 2

        return total % MOD
```
---
# Optimal Solution 
```python
class Solution:
    def numSub(self, s: str) -> int:
        ones = [string for string in s.split("0") if string]
        result = 0
        for i in range(len(ones)):
            n = len(ones[i])
            result += n*(n + 1) // 2
            # print(result)
        return result % (10**9 + 7)
```
