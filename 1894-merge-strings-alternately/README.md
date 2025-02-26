<h2><a href="https://leetcode.com/problems/merge-strings-alternately">1894. Merge Strings Alternately</a></h2><h3>Easy</h3><hr><p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<p>Return <em>the merged string.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abc&quot;, word2 = &quot;pqr&quot;
<strong>Output:</strong> &quot;apbqcr&quot;
<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;ab&quot;, word2 = &quot;pqrs&quot;
<strong>Output:</strong> &quot;apbqrs&quot;
<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, &quot;rs&quot; is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abcd&quot;, word2 = &quot;pq&quot;
<strong>Output:</strong> &quot;apbqcd&quot;
<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, &quot;cd&quot; is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>

## Solution Approach 
 * Use two pointer with the while loop to alternately append the words in the result string 
 * the solution can be improved and 
 ```python
 class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1 
        return result
```
* Improved Version of the Solution 

### Issues in the Current Code
1. String Concatenation (+=) is Slow
* Strings in Python are immutable, so every += operation creates a new string, copying all previous characters.
* This results in O(n²) time complexity, which is inefficient.
2. len(result) != len_word1 + len_word2 is Unnecessary
* You already have checks for i < len_word1 and j < len_word2, so this condition is redundant.

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while i < len_word1 or j < len_word2:
            if i < len_word1:
                result.append(word1[i])
                i += 1
            if j < len_word2:
                result.append(word2[j])
                j += 1 
        return "".join(result)
 ```
 - This can be still improved by removing j variable 
 
 ```python
 def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while i < len_word1 or i < len_word2:
            if i < len_word1:
                result.append(word1[i])
            if i < len_word2:
                result.append(word2[i])
            i += 1
        return "".join(result)
```

### Optimized Solution 

```python 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                res += word1[i]
            if i < len2:
                res += word2[i]
        
        return res
```
