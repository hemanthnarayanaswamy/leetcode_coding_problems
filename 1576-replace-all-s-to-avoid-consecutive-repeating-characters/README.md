<h2><a href="https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters">1698. Replace All ?'s to Avoid Consecutive Repeating Characters</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> containing only lowercase English letters and the <code>&#39;?&#39;</code> character, convert <strong>all </strong>the <code>&#39;?&#39;</code> characters into lowercase letters such that the final string does not contain any <strong>consecutive repeating </strong>characters. You <strong>cannot </strong>modify the non <code>&#39;?&#39;</code> characters.</p>

<p>It is <strong>guaranteed </strong>that there are no consecutive repeating characters in the given string <strong>except </strong>for <code>&#39;?&#39;</code>.</p>

<p>Return <em>the final string after all the conversions (possibly zero) have been made</em>. If there is more than one solution, return <strong>any of them</strong>. It can be shown that an answer is always possible with the given constraints.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;?zs&quot;
<strong>Output:</strong> &quot;azs&quot;
<strong>Explanation:</strong> There are 25 solutions for this problem. From &quot;azs&quot; to &quot;yzs&quot;, all are valid. Only &quot;z&quot; is an invalid modification as the string will consist of consecutive repeating characters in &quot;zzs&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ubv?w&quot;
<strong>Output:</strong> &quot;ubvaw&quot;
<strong>Explanation:</strong> There are 24 solutions for this problem. Only &quot;v&quot; and &quot;w&quot; are invalid modifications as the strings will consist of consecutive repeating characters in &quot;ubvvw&quot; and &quot;ubvww&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consist of lowercase English letters and <code>&#39;?&#39;</code>.</li>
</ul>

# Brute Force / Bad Implementation 
* We have à function  to generate `replacement of '?'`
```python
def replacement(c1, c2):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c == c1 or c == c2:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)
	# It starts to 'a' are result and check the pre and next chars of '?' and keeps iterating until it finds a char that is not equal to prev or next of '?'
```
1. We do the normal iteration from `1 - n` ignoring the initial char to replace all `?`.
   - we handle one edge case where `i = len(s)-1` for which `i + 1` doesn't exit.
```python
for i in range(1, len(s)):
            if characters[i] == '?':
                if i == len(s)-1:
                    c1 = c2 = characters[i-1]
                else:
                    c1 = characters[i-1]
                    c2 = characters[i+1]

                characters[i] = replacement(c1, c2)
```
---
```python
class Solution:
    def modifyString(self, s: str) -> str:
        def replacement(avoid):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c in avoid:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)
        n = len(s)

        for i in range(1, n):
            if characters[i] == '?':
                if i != n-1:
                    avoid = characters[i-1] + characters[i+1]
                else:
                    avoid = characters[i-1]

                characters[i] = replacement(avoid)
        
        if characters[0] == '?':
            avoid = '' if n == 1 else characters[1]
            characters[0] = replacement(avoid)
        
        return ''.join(characters)
```
---
```python
class Solution:
    def modifyString(self, s: str) -> str:
        def replacement(c1, c2):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c == c1 or c == c2:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)

        for i in range(1, len(s)):
            if characters[i] == '?':
                if i == len(s)-1:
                    c1 = c2 = characters[i-1]
                else:
                    c1 = characters[i-1]
                    c2 = characters[i+1]

                characters[i] = replacement(c1, c2)
        
        if characters[0] == '?':
            if len(s) == 1:
                return 'a'
            else:
                c1 = c2 = characters[1]
                characters[0] = replacement(c1, c2)

        
        return ''.join(characters)
```
---
# Optimal Solution 
```python
class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(res)
        
        for i in range(n):
            if res[i] == '?':
                for char in ['a', 'b', 'c']:
                    prev_char = res[i - 1] if i > 0 else None
                    next_char = res[i + 1] if i < n - 1 else None
                    
                    if char != prev_char and char != next_char:
                        res[i] = char
                        break
        
        return "".join(res)
```
---
```python
class Solution:
    def modifyString(self, s: str) -> str:
        def replacement(pc, nc):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c == pc or c == nc:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)
        n = len(s)

        for i in range(n):
            if characters[i] == '?':
                pc = characters[i - 1] if i > 0 else None
                nc = characters[i + 1] if i < n - 1 else None

                characters[i] = replacement(pc, nc)
        
        return ''.join(characters)
```
**We can do a `None` comparaison always with numbers or characters**
