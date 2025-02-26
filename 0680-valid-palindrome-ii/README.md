<h2><a href="https://leetcode.com/problems/valid-palindrome-ii">680. Valid Palindrome II</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, return <code>true</code> <em>if the </em><code>s</code><em> can be palindrome after deleting <strong>at most one</strong> character from it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abca&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> You could delete the character &#39;c&#39;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


## Solution Approach 

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        count = 0 

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                count += 1
                if count > 1:
                    return False
                else: 
                    if s[l+1] == s[r]: 
                        l += 2
                        r -= 1
                    elif s[l] == s[r-1]:
                        l += 1
                        r -= 2
                    else:
                        return False
        
        return True
``` 
* Tried this solution but could resolve some edge cases does not handle deletion properly 

#### Proper Approach 
* Use Two-Pointer Method (l, r), Compare s[l] with s[r]
* If s[l] == s[r], move inward (l += 1, r -= 1).
* If mismatch occurs, try removing either s[l] or s[r] and check if either modified substring is a palindrome.

```python 
class Solution:
    def isPalindrome(self, s: str, l: int , r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
    
        while l < r:
            if s[l] != s[r]:
            # If mismatch, check by skipping left or right character
                return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
            l += 1
            r -= 1

        return True
```
* Still can be improved by calling the `isPalindrome` from inside of the `validPalindrome`

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str, l: int , r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s)-1
    
        while l < r:
            if s[l] != s[r]:
            # If mismatch, check by skipping left or right character
                return isPalindrome(s, l+1, r) or isPalindrome(s, l, r-1)
            l += 1
            r -= 1

        return True
```
        
