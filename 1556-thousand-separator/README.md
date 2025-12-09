<h2><a href="https://leetcode.com/problems/thousand-separator/?envType=problem-list-v2&envId=n9iuhemc">1660. Thousand Separator</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, add a dot (&quot;.&quot;) as the thousands separator and return it in string format.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 987
<strong>Output:</strong> &quot;987&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1234
<strong>Output:</strong> &quot;1.234&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Solution 
* Use a count variable to track the every thounds digit place and append the `.` when the `count == 3` and make sure that it `.` is not appned at the start of the number as the count will be `3`. 
```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        nStr = str(n)
        res = []
        
        count = 0
        for i in range(len(nStr)-1, -1, -1):
            res.append(nStr[i])
            count += 1

            if count == 3 and i != 0:
                res.append('.')
                count = 0

        return ''.join(res[::-1])
```
---
```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        s=s[::-1]
        res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        return res[::-1]
```
