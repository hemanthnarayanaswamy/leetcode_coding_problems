<h2><a href="https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string">1128. Remove All Adjacent Duplicates In String</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> consisting of lowercase English letters. A <strong>duplicate removal</strong> consists of choosing two <strong>adjacent</strong> and <strong>equal</strong> letters and removing them.</p>

<p>We repeatedly make <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It can be proven that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbaca&quot;
<strong>Output:</strong> &quot;ca&quot;
<strong>Explanation:</strong> 
For example, in &quot;abbaca&quot; we could remove &quot;bb&quot; since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is &quot;aaca&quot;, of which only &quot;aa&quot; is possible, so the final string is &quot;ca&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;azxxzy&quot;
<strong>Output:</strong> &quot;ay&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

# Solution 
* My own solution, it was not a bad idea.
* compare the result last element with the strings next iteration to remove the same elements else append the unique character.

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = [s[0]]

        for i in range(1, len(s)):
            if len(result) == 0:
                result.append(s[i])

            elif result[-1] == s[i]:
                result.pop()
                
            else:
                result.append(s[i])
        
        return ''.join(result)
```

* logic can be improved

# Improved 
```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for c in s:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)
        
        return ''.join(result)
```
