<h2><a href="https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length">1567. Maximum Number of Vowels in a Substring of Given Length</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the maximum number of vowel letters in any substring of </em><code>s</code><em> with length </em><code>k</code>.</p>

<p><strong>Vowel letters</strong> in English are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abciiidef&quot;, k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring &quot;iii&quot; contains 3 vowel letters.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aeiou&quot;, k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Any substring of length 2 contains 2 vowels.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> &quot;lee&quot;, &quot;eet&quot; and &quot;ode&quot; contain 2 vowels.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>

# Wrong Solution 
* This solution is working but TLE
```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowel = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(len(s)):
            if s[i] in vowels:
                tmp = 0
                for c in s[i:i+k]:
                    if c in vowels:
                        tmp += 1
                
                if tmp == k:
                    return k
                else:
                    maxVowel = max(maxVowel, tmp)
        
        return maxVowel
```

# Solution 
* Using the Sliding Window technique, We iterate normally while keeping track of the current vowel count and the max count. 
* when `i >= k` means the window size is exceeded then we remove the last element which is `i - k` 
* If the removed element if vowel we reduce the count and as usually we keep track of the maxCount.

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        countVowel = maxVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(len(s)):
            if s[i] in vowels:
                countVowel += 1
            
            if i >= k and s[i - k] in vowels:
                countVowel -= 1
            
            if countVowel > maxVowels:
                maxVowels = countVowel

        return maxVowels
```
---
```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        countVowel = 0

        for c in s[:k]:
            if c in vowels:
                countVowel += 1
        
        maxVowels = countVowel

        for i in range(k, len(s)):
            if s[i] in vowels:
                countVowel += 1

            if s[i - k] in vowels:
                countVowel -= 1 
            
            if countVowel > maxVowels:
                maxVowels = countVowel 

        return maxVowels
```
