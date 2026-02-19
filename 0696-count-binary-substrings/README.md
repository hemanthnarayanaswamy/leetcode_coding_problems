<h2><a href="https://leetcode.com/problems/count-binary-substrings">696. Count Binary Substrings</a></h2><h3>Easy</h3><hr><p>Given a binary string <code>s</code>, return the number of non-empty substrings that have the same number of <code>0</code>&#39;s and <code>1</code>&#39;s, and all the <code>0</code>&#39;s and all the <code>1</code>&#39;s in these substrings are grouped consecutively.</p>

<p>Substrings that occur multiple times are counted the number of times they occur.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;00110011&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 substrings that have equal number of consecutive 1&#39;s and 0&#39;s: &quot;0011&quot;, &quot;01&quot;, &quot;1100&quot;, &quot;10&quot;, &quot;0011&quot;, and &quot;01&quot;.
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, &quot;00110011&quot; is not a valid substring because all the 0&#39;s (and 1&#39;s) are not grouped together.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10101&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 substrings: &quot;10&quot;, &quot;01&quot;, &quot;10&quot;, &quot;01&quot; that have equal number of consecutive 1&#39;s and 0&#39;s.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


# Wrong Solution Attemped
* I used a nested `while` loop to get the loops, which is very bad implementation. 
```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 1
        ans = []
        substr = 0

        while i < n:
            count = 1
            while i < n and s[i-1] == s[i]:
                count += 1
                i += 1
            else:
                ans.append(count)
            i += 1
				ans.append(count) # Here there is problem tracking the proper count
        
        print(ans)
        for j in range(1, len(ans)):
            substr += min(ans[j], ans[j-1])
        
        return substr
```
---
# Solution 
```python
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        ans = 0

        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                groups.append(1)
            else:
                groups[-1] += 1
        
        for i in range(len(groups)-1):
            ans += min(groups[i], groups[i+1])
        
        return ans
```        
* We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string. For example, if `s = "110001111000000"`, then `groups = [2, 3, 4, 6]`
* For every binary string of the form `'0' * k + '1' * k` or `'1' * k + '0' * k`, the middle of this string must occur between two groups.

```ini
Count valid binary strings between groups[i] and groups[i+1].
groups[i] = 2  groups[i+1] = 3 ("00111" or "11000") 

We clearly can make min(groups[i], groups[i+1]) valid binary strings within this string.
Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.
```
---
# Optimized Solution 
**Instead of storing groups, we will remember only `prev = groups[-2]` and `cur = groups[-1]`. **
**Then, the answer is the `sum of min(prev, cur)` over each different `final (prev, cur)` **

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1

        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
            print(ans)
    
        return ans + min(cur, prev)
```
