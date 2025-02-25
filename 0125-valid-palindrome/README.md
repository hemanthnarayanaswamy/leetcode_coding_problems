<h2><a href="https://leetcode.com/problems/valid-palindrome/">125. Valid Palindrome</a></h2><h3>Easy</h3><hr><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>

## Solution Approch 

### How to Clean up a string

#### Normal approach 
- Clean up the string to only have the charaters and numbers 
- reverse the string and compare 

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for char in s.lower():
            if char.isalnum():
                s2 += char
        
        return s2 == s2[::-1]
```
- More optimized Solution using the filter to filterout only required items 

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()

        return s == s[::-1]
```

#### Two Pointer Approach 
- Clean up the string 
- two pointer comparison untill left > right 

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False  
            left += 1
            right -= 1  
        return True
```

