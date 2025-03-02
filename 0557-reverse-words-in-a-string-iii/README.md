<h2><a href="https://leetcode.com/problems/reverse-words-in-a-string-iii">557. Reverse Words in a String III</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Let&#39;s take LeetCode contest&quot;
<strong>Output:</strong> &quot;s&#39;teL ekat edoCteeL tsetnoc&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Mr Ding&quot;
<strong>Output:</strong> &quot;rM gniD&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> contains printable <strong>ASCII</strong> characters.</li>
	<li><code>s</code> does not contain any leading or trailing spaces.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
	<li>All the words in <code>s</code> are separated by a single space.</li>
</ul>


## Solution Approach 
* split the string than stip each individual string inot lists and apply two pointer of it and them merger and returnt eh string.
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        result = []
        for word in s:
            word = [letter for letter in word]
            l, r = 0, len(word)-1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            
            result.append("".join(word))
        return " ".join(result)
```

### Improved Solution 
```python
def reverseword(s):
    s = s.split(" ")
    result = []
    for word in s:
        result.append(word[::-1])
    return " ".join(result)
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1].split(" ")

        return " ".join(i for i in s[::-1])
				
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())    
```
