<h2><a href="https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case">1363. Greatest English Letter in Upper and Lower Case</a></h2><h3>Easy</h3><hr><p>Given a string of English letters <code>s</code>, return <em>the <strong>greatest </strong>English letter which occurs as <strong>both</strong> a lowercase and uppercase letter in</em> <code>s</code>. The returned letter should be in <strong>uppercase</strong>. If no such letter exists, return <em>an empty string</em>.</p>

<p>An English letter <code>b</code> is <strong>greater</strong> than another letter <code>a</code> if <code>b</code> appears <strong>after</strong> <code>a</code> in the English alphabet.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;l<strong><u>Ee</u></strong>TcOd<u><strong>E</strong></u>&quot;
<strong>Output:</strong> &quot;E&quot;
<strong>Explanation:</strong>
The letter &#39;E&#39; is the only letter to appear in both lower and upper case.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a<strong><u>rR</u></strong>AzFif&quot;
<strong>Output:</strong> &quot;R&quot;
<strong>Explanation:</strong>
The letter &#39;R&#39; is the greatest letter to appear in both lower and upper case.
Note that &#39;A&#39; and &#39;F&#39; also appear in both lower and upper case, but &#39;R&#39; is greater than &#39;F&#39; or &#39;A&#39;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;AbCdEfGhIjK&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong>
There is no letter that appears in both lower and upper case.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase and uppercase English letters.</li>
</ul>

# Solution 
* A bit bad solution as it contains lot of unnecessary steps. 

```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ''

        s_map = Counter(s)

        for c in s:
            temp = ''
            if c.upper() in s_map and c.lower() in s_map:
                temp = c.upper()
            
            if temp and res:
                if ord(temp) > ord(res):
                    res = temp
            elif temp and not res:
                    res = temp
        
        return res
```

# Optimal Solution 
* Fixed 26 step loop checking membership in the seen set. 
* No need for the `ord()` 
* check from 'Z' down to 'A' that way whatever element meets the condition first if the greatest element.

```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        seen = set(s)

        for c in alphabets[::-1]: # check from 'Z' down to 'A'
            if c in seen and c.lower() in seen:
                return c

        return ''
```

```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set()
        for c in s:
            chars.add(c)

        for c in range(ord('Z'), ord('A')-1, -1):
            char = chr(c)
            if char in chars and char.lower() in chars:
                return chr(c)

        return ""
```

