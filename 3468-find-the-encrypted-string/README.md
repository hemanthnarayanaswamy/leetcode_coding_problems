<h2><a href="https://leetcode.com/problems/find-the-encrypted-string">3468. Find the Encrypted String</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> and an integer <code>k</code>. Encrypt the string using the following algorithm:</p>

<ul>
	<li>For each character <code>c</code> in <code>s</code>, replace <code>c</code> with the <code>k<sup>th</sup></code> character after <code>c</code> in the string (in a cyclic manner).</li>
</ul>

<p>Return the <em>encrypted string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;dart&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;tdar&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>, the 3<sup>rd</sup> character after <code>&#39;d&#39;</code> is <code>&#39;t&#39;</code>.</li>
	<li>For <code>i = 1</code>, the 3<sup>rd</sup> character after <code>&#39;a&#39;</code> is <code>&#39;d&#39;</code>.</li>
	<li>For <code>i = 2</code>, the 3<sup>rd</sup> character after <code>&#39;r&#39;</code> is <code>&#39;a&#39;</code>.</li>
	<li>For <code>i = 3</code>, the 3<sup>rd</sup> character after <code>&#39;t&#39;</code> is <code>&#39;r&#39;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aaa&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aaa&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>As all the characters are the same, the encrypted string will also be the same.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

# Solution 
```python
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = ''
        n = len(s)

        for i in range(n):
            encrypted = i+k

            while encrypted >= n:
                encrypted -= n

            res += s[encrypted]
        
        return res
```

# Optimal Solution 
* The goal is to shift each character in the string by k positions forward. If k is greater than the string's length, we only need to shift by k % n positions, where n is the length of the string. This is because shifting by the length of the string brings us back to the start.

### Approach
1. Calculate the effective shift as k % n to handle cases where k is larger than the length of the string n.
2. Create an array to hold the characters of the encrypted string.
3. Loop through each character in the string.
      * For each character at position i, find its new position as (i + k) % n.
      * Place the character in the new position in the result array.
4. Combine the characters in the result array to form the final encrypted string.

```python
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        if n == 0:
            return s
        r = k % n
        out = [''] * n
        for i, ch in enumerate(s):
            out[i] = s[(i + r) % n]
        return ''.join(out)
```
