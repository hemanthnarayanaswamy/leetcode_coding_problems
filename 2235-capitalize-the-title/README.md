<h2><a href="https://leetcode.com/problems/capitalize-the-title">2235. Capitalize the Title</a></h2><h3>Easy</h3><hr><p>You are given a string <code>title</code> consisting of one or more words separated by a single space, where each word consists of English letters. <strong>Capitalize</strong> the string by changing the capitalization of each word such that:</p>

<ul>
	<li>If the length of the word is <code>1</code> or <code>2</code> letters, change all letters to lowercase.</li>
	<li>Otherwise, change the first letter to uppercase and the remaining letters to lowercase.</li>
</ul>

<p>Return <em>the <strong>capitalized</strong> </em><code>title</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> title = &quot;capiTalIze tHe titLe&quot;
<strong>Output:</strong> &quot;Capitalize The Title&quot;
<strong>Explanation:</strong>
Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> title = &quot;First leTTeR of EACH Word&quot;
<strong>Output:</strong> &quot;First Letter of Each Word&quot;
<strong>Explanation:</strong>
The word &quot;of&quot; has length 2, so it is all lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> title = &quot;i lOve leetcode&quot;
<strong>Output:</strong> &quot;i Love Leetcode&quot;
<strong>Explanation:</strong>
The word &quot;i&quot; has length 1, so it is lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= title.length &lt;= 100</code></li>
	<li><code>title</code> consists of words separated by a single space without any leading or trailing spaces.</li>
	<li>Each word consists of uppercase and lowercase English letters and is <strong>non-empty</strong>.</li>
</ul>

# Solution 
* Access of element in the list is O(n), so make to reuse it instead of assessing it again and again 
* Re-use the variable 
```python
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()

        for i in range(len(title)):
            word = title[i]
            if len(word) > 2:
                title[i] = word.capitalize()
            else:
                title[i] = word.lower()
        
        return " ".join(title)
```

```python
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = []
        for i in words:
            if len(i) < 3: result.append(i.lower())
            else: result.append(i.capitalize())
        return ' '.join(result)
```
