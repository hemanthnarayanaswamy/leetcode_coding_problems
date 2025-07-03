<h2><a href="https://leetcode.com/problems/delete-characters-to-make-fancy-string">1302. Delete Characters to Make Fancy String</a></h2><h3>Easy</h3><hr><p>A <strong>fancy string</strong> is a string where no <strong>three</strong> <strong>consecutive</strong> characters are equal.</p>

<p>Given a string <code>s</code>, delete the <strong>minimum</strong> possible number of characters from <code>s</code> to make it <strong>fancy</strong>.</p>

<p>Return <em>the final string after the deletion</em>. It can be shown that the answer will always be <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;le<u>e</u>etcode&quot;
<strong>Output:</strong> &quot;leetcode&quot;
<strong>Explanation:</strong>
Remove an &#39;e&#39; from the first group of &#39;e&#39;s to create &quot;leetcode&quot;.
No three consecutive characters are equal, so return &quot;leetcode&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;<u>a</u>aab<u>aa</u>aa&quot;
<strong>Output:</strong> &quot;aabaa&quot;
<strong>Explanation:</strong>
Remove an &#39;a&#39; from the first group of &#39;a&#39;s to create &quot;aabaaaa&quot;.
Remove two &#39;a&#39;s from the second group of &#39;a&#39;s to create &quot;aabaa&quot;.
No three consecutive characters are equal, so return &quot;aabaa&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;
<strong>Output:</strong> &quot;aab&quot;
<strong>Explanation:</strong> No three consecutive characters are equal, so return &quot;aab&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

# Solution 
* Append the first character into the result array and check if `i, i-1, i+1` are equal if they are equal continue skipping the current char else append the char. 
```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        fancyStr = [s[0]]

        for i in range(1, len(s)):
            if i + 1 == len(s):
                fancyStr.append(s[i])
                continue 

            if s[i] == s[i-1] == s[i+1]:
                continue 
            fancyStr.append(s[i])
        
        return ''.join(fancyStr)
```
* Avoid the index Juggling and special Cases at the start and end. 

# Improved Solution 
```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)< 3: return s

        res = [s[0], s[1]]

        for i in range(2, len(s)):
            if res[-2] == res[-1] == s[i]:
                continue
            res.append(s[i])
        
        return ''.join(res)
```

# Optimal Solution
```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)< 3: return s
        a = s[0]
        b = s[1]
        res = [a, b]
        for c in s[2:]:
            if c == b == a:
                continue
            else:
                res.append(c)
            a, b = b, c
        return res
```
