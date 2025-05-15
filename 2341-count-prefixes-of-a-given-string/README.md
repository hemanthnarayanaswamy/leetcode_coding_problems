<h2><a href="https://leetcode.com/problems/count-prefixes-of-a-given-string">2341. Count Prefixes of a Given String</a></h2><h3>Easy</h3><hr><p>You are given a string array <code>words</code> and a string <code>s</code>, where <code>words[i]</code> and <code>s</code> comprise only of <strong>lowercase English letters</strong>.</p>

<p>Return <em>the <strong>number of strings</strong> in</em> <code>words</code> <em>that are a <strong>prefix</strong> of</em> <code>s</code>.</p>

<p>A <strong>prefix</strong> of a string is a substring that occurs at the beginning of the string. A <b>substring</b> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;ab&quot;,&quot;bc&quot;,&quot;abc&quot;], s = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The strings in words which are a prefix of s = &quot;abc&quot; are:
&quot;a&quot;, &quot;ab&quot;, and &quot;abc&quot;.
Thus the number of strings in words which are a prefix of s is 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;a&quot;], s = &quot;aa&quot;
<strong>Output:</strong> 2
<strong>Explanation:
</strong>Both of the strings are a prefix of s. 
Note that the same string can occur multiple times in words, and it should be counted each time.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length, s.length &lt;= 10</code></li>
	<li><code>words[i]</code> and <code>s</code> consist of lowercase English letters <strong>only</strong>.</li>
</ul>

# Solution
* Use counter to put the freqency of all the words to the hashMap. 
* Next do a while loop using a single pointer which tracks and prefix 
* and using string slicing find if that prefixed string is in the hashMap if it is found then append the value from the Frequency work hashMap
* return the tracked sum result 

```python
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        wordsFreq = Counter(words)
        prefixCount = 0
        i = 0
        while i < len(s):
            pre = s[:i+1]
            if pre in wordsFreq:
                prefixCount += wordsFreq[pre]
            i += 1
        
        return prefixCount
```
