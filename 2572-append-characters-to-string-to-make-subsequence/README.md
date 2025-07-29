<h2><a href="https://leetcode.com/problems/append-characters-to-string-to-make-subsequence">2572. Append Characters to String to Make Subsequence</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>s</code> and <code>t</code> consisting of only lowercase English letters.</p>

<p>Return <em>the minimum number of characters that need to be appended to the end of </em><code>s</code><em> so that </em><code>t</code><em> becomes a <strong>subsequence</strong> of </em><code>s</code>.</p>

<p>A <strong>subsequence</strong> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;coaching&quot;, t = &quot;coding&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> Append the characters &quot;ding&quot; to the end of s so that s = &quot;coachingding&quot;.
Now, t is a subsequence of s (&quot;<u><strong>co</strong></u>aching<u><strong>ding</strong></u>&quot;).
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcde&quot;, t = &quot;a&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> t is already a subsequence of s (&quot;<u><strong>a</strong></u>bcde&quot;).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;z&quot;, t = &quot;abcde&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> Append the characters &quot;abcde&quot; to the end of s so that s = &quot;zabcde&quot;.
Now, t is a subsequence of s (&quot;z<u><strong>abcde</strong></u>&quot;).
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

# Solution 
* We need to use two pointer one for s and other for t. 
* Go over one character after other if the characters match then increment pointer else only increment s pointer. 

Now the number of characters required are where the t pointer stopped, we need to append `t[i:]` characters to s to make its a substring

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        char_count = 0
        si, ti = 0, 0

        while ti < len(t):
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                si += 1
            
            if si == len(s):
                return len(t[ti:])
        
        return 0
```

# Improved Solution 
```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si, ti = 0, 0

        if s == t or not t:
            return 0
        
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1  
            si += 1  
        
        return len(t) - ti
```

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not t or s == t:
            return 0

        ti = 0
        for c in s:
            if c == t[ti]:
                ti += 1
                if ti == len(t):
                    return 0
                    
        return len(t) - ti
```
