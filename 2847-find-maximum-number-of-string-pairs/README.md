<h2><a href="https://leetcode.com/problems/find-maximum-number-of-string-pairs">2847. Find Maximum Number of String Pairs</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> array <code>words</code> consisting of <strong>distinct</strong> strings.</p>

<p>The string <code>words[i]</code> can be paired with the string <code>words[j]</code> if:</p>

<ul>
	<li>The string <code>words[i]</code> is equal to the reversed string of <code>words[j]</code>.</li>
	<li><code>0 &lt;= i &lt; j &lt; words.length</code>.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of pairs that can be formed from the array </em><code>words</code><em>.</em></p>

<p>Note that&nbsp;each string can belong in&nbsp;<strong>at most one</strong> pair.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;cd&quot;,&quot;ac&quot;,&quot;dc&quot;,&quot;ca&quot;,&quot;zz&quot;]
<strong>Output:</strong> 2
<strong>Explanation:</strong> In this example, we can form 2 pair of strings in the following way:
- We pair the 0<sup>th</sup> string with the 2<sup>nd</sup> string, as the reversed string of word[0] is &quot;dc&quot; and is equal to words[2].
- We pair the 1<sup>st</sup> string with the 3<sup>rd</sup> string, as the reversed string of word[1] is &quot;ca&quot; and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;ab&quot;,&quot;ba&quot;,&quot;cc&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> In this example, we can form 1 pair of strings in the following way:
- We pair the 0<sup>th</sup> string with the 1<sup>st</sup> string, as the reversed string of words[1] is &quot;ab&quot; and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;aa&quot;,&quot;ab&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this example, we are unable to form any pair of strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>words[i].length == 2</code></li>
	<li><code>words</code>&nbsp;consists of distinct strings.</li>
	<li><code>words[i]</code>&nbsp;contains only lowercase English letters.</li>
</ul>

# Solution 
* Simple Solution check if the reverse string is in the set if then increment count else add that string into the `set()`
* Notice that array words consist of distinct strings.

```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        uniq = set()
        count = 0

        for word in words:
            if word[::-1] in uniq:
               count += 1
            else:
                uniq.add(word)

        return count 
```

```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        seen = set()
        for word in words:
            revWord = word[::-1]
            if revWord in seen:
                cnt += 1
            seen.add(word)
        return cnt
```
