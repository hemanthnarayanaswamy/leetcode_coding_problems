<h2><a href="https://leetcode.com/problems/excel-sheet-column-number">171. Excel Sheet Column Number</a></h2><h3>Easy</h3><hr><p>Given a string <code>columnTitle</code> that represents the column title as appears in an Excel sheet, return <em>its corresponding column number</em>.</p>

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
<strong>Input:</strong> columnTitle = &quot;A&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> columnTitle = &quot;AB&quot;
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> columnTitle = &quot;ZY&quot;
<strong>Output:</strong> 701
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= columnTitle.length &lt;= 7</code></li>
	<li><code>columnTitle</code> consists only of uppercase English letters.</li>
	<li><code>columnTitle</code> is in the range <code>[&quot;A&quot;, &quot;FXSHRXW&quot;]</code>.</li>
</ul>

# Approach 
* Refer to this URL to check and observer the patters https://www.vishalon.net/blog/excel-column-letter-to-number-quick-reference

```ini
Treat the column value as a base 26 number. Map A to 1, B to 2..., and Z to 26.

AF = (1^26)*1 + 6
BF = (1^26)*2 + 6
CF = (1^26)*3 + 6
.
.
.
ZF = (1^26)*26 + 6
AAF = (2^26)*1+(1^26)*1 + 6(0^26)
BAF = (26 ^ 2)*2 + (26 ^ 1) * 1 + (26 ^ 0) * 6
```

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        temp = columnTitle[::-1]
        columnNum = 0

        for i in range(len(temp)):
            columnNum += (26 ** i)*(ord(temp[i])-64)
        
        return columnNum
```
* for the Above solution you can use `reversed()` directly in the for loop for iterations 

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans
```

# Optimal Solution 
```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = (result * 26) + (ord(char)-ord('A')+1)
        return result
```
