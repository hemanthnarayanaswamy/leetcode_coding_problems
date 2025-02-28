<h2><a href="https://leetcode.com/problems/find-first-palindromic-string-in-the-array">2231. Find First Palindromic String in the Array</a></h2><h3>Easy</h3><hr><p>Given an array of strings <code>words</code>, return <em>the first <strong>palindromic</strong> string in the array</em>. If there is no such string, return <em>an <strong>empty string</strong> </em><code>&quot;&quot;</code>.</p>

<p>A string is <strong>palindromic</strong> if it reads the same forward and backward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abc&quot;,&quot;car&quot;,&quot;ada&quot;,&quot;racecar&quot;,&quot;cool&quot;]
<strong>Output:</strong> &quot;ada&quot;
<strong>Explanation:</strong> The first string that is palindromic is &quot;ada&quot;.
Note that &quot;racecar&quot; is also palindromic, but it is not the first.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;notapalindrome&quot;,&quot;racecar&quot;]
<strong>Output:</strong> &quot;racecar&quot;
<strong>Explanation:</strong> The first and only string that is palindromic is &quot;racecar&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;def&quot;,&quot;ghi&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There are no palindromic strings, so the empty string is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
</ul>

## Solution Approach 

```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s):  ## Wrote a function inside class like I learned to process the palindrom seperately 
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return ''
                r -= 1
                l += 1
            return s 
        
        for word in words: 
            if is_palindrome(word):
                return word
        return ''
```

* Using the Array Slicing Tecchnique 
```python
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''
```
