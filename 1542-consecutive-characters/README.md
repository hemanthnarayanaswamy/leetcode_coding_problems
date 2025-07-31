<h2><a href="https://leetcode.com/problems/consecutive-characters">1542. Consecutive Characters</a></h2><h3>Easy</h3><hr><p>The <strong>power</strong> of the string is the maximum length of a non-empty substring that contains only one unique character.</p>

<p>Given a string <code>s</code>, return <em>the <strong>power</strong> of</em> <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The substring &quot;ee&quot; is of length 2 with the character &#39;e&#39; only.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbcccddddeeeeedcba&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The substring &quot;eeeee&quot; is of length 5 with the character &#39;e&#39; only.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

# Solution 
```python
class Solution:
    def maxPower(self, s: str) -> int:
        max_power = current_power = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_power += 1
            else:
                max_power = max(max_power, current_power)
                current_power = 1
        
        return max(max_power, current_power)
```

# Improved Solution 
```python
class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        cur = 0
        curr_c = None
        for c in s:
            if c != curr_c:
                curr_c = c
                cur = 1
            else:
                cur += 1
            if cur > res:
                res = cur
        return res
```
