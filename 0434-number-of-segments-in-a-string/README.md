<h2><a href="https://leetcode.com/problems/number-of-segments-in-a-string">434. Number of Segments in a String</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, return <em>the number of segments in the string</em>.</p>

<p>A <strong>segment</strong> is defined to be a contiguous sequence of <strong>non-space characters</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Hello, my name is John&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The five segments are [&quot;Hello,&quot;, &quot;my&quot;, &quot;name&quot;, &quot;is&quot;, &quot;John&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Hello&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 300</code></li>
	<li><code>s</code> consists of lowercase and uppercase English letters, digits, or one of the following characters <code>&quot;!@#$%^&amp;*()_+-=&#39;,.:&quot;</code>.</li>
	<li>The only space character in <code>s</code> is <code>&#39; &#39;</code>.</li>
</ul>

# Solution 
* Just need to split the array and compute the length which gives the number of segments in the string 

```python
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
```

```python
class Solution:
    def countSegments(self, s: str) -> int:
        r = s.split(' ')
        r = [x for x in r if x]
        return len(r)
```
## Note 
`s.split() — Smart Split`
* Splits on any whitespace (space, tab, newline, etc.)
* Ignores multiple consecutive spaces
* Ignores leading and trailing whitespace
* Useful for natural language-style splitting
---------
`s.split(' ') — Literal Split`
* Only splits on literal space characters ' '
* Does NOT ignore empty strings if there are multiple spaces
* Preserves empty splits caused by multiple or trailing spaces

```python
s = "  Hello   world   "

>>> s.split()
['Hello', 'world']
>>> len(s.split())
2

>>> s.split(' ')
['', '', 'Hello', '', '', 'world', '', '', '']
>>> len(s.split(' '))
9
```
