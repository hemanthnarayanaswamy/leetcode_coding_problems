<h2><a href="https://leetcode.com/problems/excel-sheet-column-title">168. Excel Sheet Column Title</a></h2><h3>Easy</h3><hr><p>Given an integer <code>columnNumber</code>, return <em>its corresponding column title as it appears in an Excel sheet</em>.</p>

<p>For example:</p>

<pre>
A -&gt; 1
B -&gt; 2
C -&gt; 3
...
Z -&gt; 26
AA -&gt; 27
AB -&gt; 28 
...
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 28
<strong>Output:</strong> &quot;AB&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 701
<strong>Output:</strong> &quot;ZY&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= columnNumber &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Solution 
1. Initialize an empty string ans which would store the column title.
2. Do the following as long as columnNumber is greater than 0:
- Subtract 1 from the columnNumber
- Find the character corresponding to columnNumber % 26 and append it to the ans in the end.
- Assign columnNumber to columnNumber / 26.
3. Reverse the string columnNumber and return it.


https://leetcode.com/problems/excel-sheet-column-title/editorial/?envType=problem-list-v2&envId=n9iuhemc#approach-convert

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            # Get the last character and append it at the end of string.
            ans += chr(columnNumber % 26 + ord("A"))
            columnNumber //= 26

        # Reverse it, as we appended characters in reverse order.
        return ans[::-1]
```
