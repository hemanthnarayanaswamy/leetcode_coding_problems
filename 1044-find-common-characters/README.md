<h2><a href="https://leetcode.com/problems/find-common-characters">1044. Find Common Characters</a></h2><h3>Easy</h3><hr><p>Given a string array <code>words</code>, return <em>an array of all characters that show up in all strings within the </em><code>words</code><em> (including duplicates)</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["bella","label","roller"]
<strong>Output:</strong> ["e","l","l"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["cool","lock","cook"]
<strong>Output:</strong> ["c","o"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

# Note:
* When using Counter, you can compare the values which doesn't exist in the HashMap also which will return zero by default without throwing the errors. 

```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        commonCharacters = Counter(words[0])
        n = len(words)

        for i in range(1, n):
            currentCharacters = Counter(words[i])

            for ch in commonCharacters:
# Here we are using the Counter functionality to compara the counts even when the character doesn't exists in one or other, without throwing the errors. 
                commonCharacters[ch] = min(currentCharacters[ch], commonCharacters[ch])
        
        for k, v in commonCharacters.items():
            while v:
                res.append(k)
                v -= 1
        
        return res
```
---
# Optimal Solution 
* Use `Counter Intersection` and `elements()`

```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        c = Counter(words[0])

        for w in words[1:]:
            c &= Counter(w)           # min per character
              
        return list(c.elements())     # expand by counts
```
---
```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = list(words[0])
        for word in words[1:]:
            new_result = []
            for ch in word:
                if ch in result:
                    new_result.append(ch)
                    result.remove(ch)
            result = new_result
        return result
```
