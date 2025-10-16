<h2><a href="https://leetcode.com/problems/license-key-formatting">482. License Key Formatting</a></h2><h3>Easy</h3><hr><p>You are given a license key represented as a string <code>s</code> that consists of only alphanumeric characters and dashes. The string is separated into <code>n + 1</code> groups by <code>n</code> dashes. You are also given an integer <code>k</code>.</p>

<p>We want to reformat the string <code>s</code> such that each group contains exactly <code>k</code> characters, except for the first group, which could be shorter than <code>k</code> but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.</p>

<p>Return <em>the reformatted license key</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;5F3Z-2e-9-w&quot;, k = 4
<strong>Output:</strong> &quot;5F3Z-2E9W&quot;
<strong>Explanation:</strong> The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;2-5g-3-J&quot;, k = 2
<strong>Output:</strong> &quot;2-5G-3J&quot;
<strong>Explanation:</strong> The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of English letters, digits, and dashes <code>&#39;-&#39;</code>.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

# Solution 
1. Remove all the `'-'`;
2. Reverse the string
3. If some char is lower convert it to upper
4. when `i%k==0` add `'-'` else keep on adding normally to the string ;
5. At the end reverse the string you built and return.

```python
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sNew = s.replace('-', '')[::-1]
        n = len(sNew)

        if n == 0 or n < k:
            return sNew.upper()[::-1]
        
        res = []

        for i in range(n):
            if i != 0 and i % k == 0:
                res.append('-')
            res.append(sNew[i].upper())
        
        return ''.join(res)[::-1]
```
---
# Optimal Solution 
```python
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sNew = s.replace('-', '')[::-1]
        n = len(sNew)

        if n == 0:
            return ""
        elif n <= k:
            return sNew[::-1].upper()   
        
        parts = [sNew[i:i+k] for i in range(0, n, k)]
				print(parts) # ['J3', 'g5', '2']
        formattedKey = '-'.join(parts)[::-1].upper()
        return formattedKey 
```
