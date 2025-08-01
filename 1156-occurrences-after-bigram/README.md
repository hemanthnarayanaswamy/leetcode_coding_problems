<h2><a href="https://leetcode.com/problems/occurrences-after-bigram">1156. Occurrences After Bigram</a></h2><h3>Easy</h3><hr><p>Given two strings <code>first</code> and <code>second</code>, consider occurrences in some text of the form <code>&quot;first second third&quot;</code>, where <code>second</code> comes immediately after <code>first</code>, and <code>third</code> comes immediately after <code>second</code>.</p>

<p>Return <em>an array of all the words</em> <code>third</code> <em>for each occurrence of</em> <code>&quot;first second third&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> text = "alice is a good girl she is a good student", first = "a", second = "good"
<strong>Output:</strong> ["girl","student"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> text = "we will we will rock you", first = "we", second = "will"
<strong>Output:</strong> ["we","rock"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 1000</code></li>
	<li><code>text</code> consists of lowercase English letters and spaces.</li>
	<li>All the words in <code>text</code> are separated by <strong>a single space</strong>.</li>
	<li><code>1 &lt;= first.length, second.length &lt;= 10</code></li>
	<li><code>first</code> and <code>second</code> consist of lowercase English letters.</li>
	<li><code>text</code> will not have any leading or trailing spaces.</li>
</ul>

# Optimal Solution 
* Clean and simple solution, split the string and use 2 variables to track the first and second things, and keep moving them. 

```python
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textLst = text.split()
        a, b = textLst[0], textLst[1]
        res = []

        for word in textLst[2::]:
            if a == first and b == second:
                res.append(word)
            
            a, b = b, word
        
        return res
```
