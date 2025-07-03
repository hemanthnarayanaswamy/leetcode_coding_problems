<h2><a href="https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/?envType=problem-list-v2&envId=n9iuhemc">2243. Check if All A's Appears Before All B's</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> consisting of <strong>only</strong> the characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code>, return <code>true</code> <em>if <strong>every</strong> </em><code>&#39;a&#39;</code> <em>appears before <strong>every</strong> </em><code>&#39;b&#39;</code><em> in the string</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabbb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>
The &#39;a&#39;s are at indices 0, 1, and 2, while the &#39;b&#39;s are at indices 3, 4, and 5.
Hence, every &#39;a&#39; appears before every &#39;b&#39; and we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong>
There is an &#39;a&#39; at index 2 and a &#39;b&#39; at index 1.
Hence, not every &#39;a&#39; appears before every &#39;b&#39; and we return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>
There are no &#39;a&#39;s, hence, every &#39;a&#39; appears before every &#39;b&#39; and we return true.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is either <code>&#39;a&#39;</code> or <code>&#39;b&#39;</code>.</li>
</ul>

# Solution 
* We will have a counter with total number of A's and iterate throught the string.
* If A is detected then we'll reduce the counter , If B is detercted then we check the A's counter if its zero or not.

```python
class Solution:
    def checkString(self, s: str) -> bool:
        countA = s.count('a')

        for c in s:
            if c == 'b' and countA != 0:
                return False
            elif c == 'a':
                countA -= 1
        
        return True
```

# Updated Solution 
* Instead of having the counter values use a flag to indicate the seen value. 
```python
class Solution:
    def checkString(self, s: str) -> bool:
        seenB = False 

        for c in s:
            if c == 'b':
                seenB = True
            elif seenB: # check c == a after already seen b
                return False
        
        return True
```

```python
class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s
```
# Optimal Solution 
```python
b = s.find('b')      # index of the first 'b' in s, or -1 if none
a = s.rfind('a')     # index of the last 'a' in s, or -1 if none

return b == -1 or a < b
```
```ini 
The condition b == -1 or a < b means:

b == -1: there are **no 'b'**s in the string, so it’s trivially all 'a's (or empty), which is valid.

a < b: the last 'a' occurs before the first 'b', so there is no interleaving “a after b.”

If neither holds (b ≠ -1 and a ≥ b), that means there’s at least one 'b', and there’s an 'a' at or after that first 'b', so the string fails the “all a’s before any b” check.
```
