<h2><a href="https://leetcode.com/problems/longest-palindrome">409. Longest Palindrome</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> which consists of lowercase or uppercase letters, return the length of the <strong>longest <span data-keyword="palindrome-string">palindrome</span></strong>&nbsp;that can be built with those letters.</p>

<p>Letters are <strong>case sensitive</strong>, for example, <code>&quot;Aa&quot;</code> is not considered a palindrome.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abccccdd&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> One longest palindrome that can be built is &quot;dccaccd&quot;, whose length is 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest palindrome that can be built is &quot;a&quot;, whose length is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase <strong>and/or</strong> uppercase English&nbsp;letters only.</li>
</ul>

# Solution 
* No need to build the palindrome, We ONLY NEED TO DETERMINE IF IT IS POSSIBLE TO CONSTRUCT THE PALINDROME. 
* To be a PALINDROME THE FREQUENCY OF THE ELEMENTS SHOULD BE EVEN. 
* If it is odd then change that to near even number by reducing the count. 
* But in the palindrome we can have à single middle element whose frequency can be odd, So use a Flag to allow only one odd frequency element and then set that flag to false. 


```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sFreq = Counter(s)
        count = 0
        middle = True

        for _, v in sFreq.items():
            if v % 2:
                if middle: 
                    count += v
                    middle = False
                else:
                    count += v - 1
            else: 
                count += v
        
        return count
```

# Improved Solution 
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sFreq = Counter(s)
        count = 0
        has_odd = False

        for freq in sFreq.values():
            count += freq // 2 * 2  # Add pairs (even count)
            if freq % 2 == 1:
                has_odd = True
        
        return count + (1 if has_odd else 0)
```
